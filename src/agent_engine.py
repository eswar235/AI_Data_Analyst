import json

from src.ai_engine import ask_llama


def create_analysis_plan(
    df,
    question
):

    columns = df.columns.tolist()

    numeric_columns = (
        df.select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    categorical_columns = (
        df.select_dtypes(
            include=[
                "object",
                "string",
                "category"
            ]
        )
        .columns
        .tolist()
    )

    prompt = f"""
You are an AI Data Analyst planning a dataframe analysis.

Available columns:

{json.dumps(columns, indent=2)}

Numerical columns:

{json.dumps(numeric_columns, indent=2)}

Categorical columns:

{json.dumps(categorical_columns, indent=2)}

User question:

{question}

Choose the best analytical operation.

Return ONLY valid JSON.

Allowed operations:

- total
- average
- median
- minimum
- maximum
- count
- top_n
- bottom_n
- group_sum
- group_average
- group_count
- unique_count
- missing_values
- duplicate_count
- overview
- unsupported

JSON format:

{{
    "operation": "operation_name",
    "column": "column_name_or_null",
    "group_by": "column_name_or_null",
    "n": 5
}}

Do not invent column names.
"""

    response = ask_llama(prompt)

    try:

        start = response.find("{")
        end = response.rfind("}") + 1

        json_text = response[
            start:end
        ]

        plan = json.loads(
            json_text
        )

        return plan

    except Exception:

        return {
            "operation": "unsupported",
            "column": None,
            "group_by": None,
            "n": 5
        }


def execute_analysis(
    df,
    plan
):

    operation = plan.get(
        "operation"
    )

    column = plan.get(
        "column"
    )

    group_by = plan.get(
        "group_by"
    )

    n = plan.get(
        "n",
        5
    )


    # ==========================================
    # VALIDATE COLUMNS
    # ==========================================

    if (
        column
        and column not in df.columns
    ):

        return (
            False,
            f"Column '{column}' "
            f"does not exist."
        )


    if (
        group_by
        and group_by not in df.columns
    ):

        return (
            False,
            f"Column '{group_by}' "
            f"does not exist."
        )


    # ==========================================
    # OVERVIEW
    # ==========================================

    if operation == "overview":

        result = {
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": int(
                df.isnull()
                .sum()
                .sum()
            ),
            "duplicate_rows": int(
                df.duplicated()
                .sum()
            )
        }

        return True, result


    # ==========================================
    # MISSING VALUES
    # ==========================================

    if operation == "missing_values":

        result = (
            df.isnull()
            .sum()
            .sort_values(
                ascending=False
            )
        )

        return True, result.to_dict()


    # ==========================================
    # DUPLICATES
    # ==========================================

    if operation == "duplicate_count":

        return True, int(
            df.duplicated()
            .sum()
        )


    # ==========================================
    # UNIQUE COUNT
    # ==========================================

    if operation == "unique_count":

        if not column:

            return (
                False,
                "No column specified."
            )

        return True, int(
            df[column]
            .nunique()
        )


    # ==========================================
    # COUNT
    # ==========================================

    if operation == "count":

        return True, len(df)


    # ==========================================
    # NUMERICAL AGGREGATIONS
    # ==========================================

    if operation in [
        "total",
        "average",
        "median",
        "minimum",
        "maximum"
    ]:

        if not column:

            return (
                False,
                "No numerical column specified."
            )

        if not (
            df[column]
            .dtype.kind
            in "biufc"
        ):

            return (
                False,
                f"'{column}' is not numerical."
            )


        series = (
            df[column]
            .dropna()
        )


        if series.empty:

            return (
                False,
                f"No valid values found in "
                f"'{column}'."
            )


        if operation == "total":

            result = series.sum()


        elif operation == "average":

            result = series.mean()


        elif operation == "median":

            result = series.median()


        elif operation == "minimum":

            result = series.min()


        else:

            result = series.max()


        return True, float(result)


    # ==========================================
    # TOP N
    # ==========================================

    if operation == "top_n":

        if not column:

            return (
                False,
                "No column specified."
            )


        result = (
            df.sort_values(
                column,
                ascending=False
            )
            .head(int(n))
        )


        return True, result


    # ==========================================
    # BOTTOM N
    # ==========================================

    if operation == "bottom_n":

        if not column:

            return (
                False,
                "No column specified."
            )


        result = (
            df.sort_values(
                column,
                ascending=True
            )
            .head(int(n))
        )


        return True, result


    # ==========================================
    # GROUP SUM
    # ==========================================

    if operation == "group_sum":

        if not column or not group_by:

            return (
                False,
                "Both metric and grouping columns "
                "are required."
            )


        result = (
            df.groupby(
                group_by
            )[column]
            .sum()
            .sort_values(
                ascending=False
            )
        )


        return True, result


    # ==========================================
    # GROUP AVERAGE
    # ==========================================

    if operation == "group_average":

        if not column or not group_by:

            return (
                False,
                "Both metric and grouping columns "
                "are required."
            )


        result = (
            df.groupby(
                group_by
            )[column]
            .mean()
            .sort_values(
                ascending=False
            )
        )


        return True, result


    # ==========================================
    # GROUP COUNT
    # ==========================================

    if operation == "group_count":

        if not group_by:

            return (
                False,
                "A grouping column is required."
            )


        result = (
            df[group_by]
            .value_counts()
        )


        return True, result


    # ==========================================
    # UNSUPPORTED
    # ==========================================

    return (
        False,
        "This question is not supported "
        "by the current analysis engine."
    )