import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llama3.2:3b"


def generate_business_insights(
    dataset_summary
):

    ai_context = dataset_summary.get(
        "ai_context",
        ""
    )

    prompt = f"""
You are a Senior Data Analyst preparing an executive analysis.

Analyze the uploaded dataset using ONLY the dataset information
provided below.

Do not invent facts, numbers, trends, causes, or business information.

DATASET CONTEXT:

{ai_context}

Create an executive-level analysis with the following sections:

## Executive Summary

Give a short summary of what the dataset contains and the most
important observations.

## Key Findings

Identify 3 to 5 important findings supported by the available data.

## Strongest Areas

Identify the strongest-performing categories, metrics, or areas
when the available data supports this.

## Potential Problems

Identify unusual values, missing data, weak performance, or other
potential issues that can be supported by the dataset.

Do NOT claim that a pattern has a specific business cause unless
the dataset provides evidence for that cause.

## Business Recommendations

Provide practical recommendations based only on the available
evidence.

## Further Analysis

Suggest additional analysis that a Data Analyst should perform
before making important business decisions.

IMPORTANT:

- Use actual numbers from the dataset context when available.
- Clearly distinguish facts from interpretations.
- Do not make up information.
- If information is insufficient, say so.
- Keep the response professional and concise.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        return result.get(
            "response",
            "The AI did not return a response."
        )

    except requests.exceptions.ConnectionError:

        return (
            "❌ Could not connect to Ollama. "
            "Make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        return (
            "⏳ The AI analysis took too long. "
            "Try again or use a smaller dataset."
        )

    except Exception as e:

        return (
            f"❌ Business insight generation failed: {str(e)}"
        )