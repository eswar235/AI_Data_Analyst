import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_llama(prompt):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "No response generated."
        )

    except requests.exceptions.ConnectionError:

        return (
            "❌ Ollama is not running. "
            "Please start Ollama and try again."
        )

    except Exception as e:

        return (
            f"❌ AI error: {str(e)}"
        )


def generate_analysis(
    dataset_summary,
    question
):

    prompt = f"""
You are an AI Data Analyst.

You are analyzing a user-provided dataset.

IMPORTANT RULES:

1. Use only the information provided below.
2. Do not invent numbers.
3. Do not invent columns.
4. Do not assume information that is not available.
5. If the available information is insufficient, clearly say so.
6. Separate facts from possible explanations.
7. Give concise, professional answers.
8. Use Markdown formatting.
9. If calculations are already provided, use those exact values.

DATASET INFORMATION:

{json.dumps(
    dataset_summary,
    indent=2,
    default=str
)}

USER QUESTION:

{question}

Provide the best possible Data Analyst response.
"""

    return ask_llama(prompt)