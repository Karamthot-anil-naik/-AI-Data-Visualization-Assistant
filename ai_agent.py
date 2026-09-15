import json
import os
from dotenv import load_dotenv
import ollama

load_dotenv()


def get_ollama_client():
    """
    Create an Ollama Cloud client from the configured API key.
    """

    api_key = os.getenv("OLLAMA_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OLLAMA_API_KEY is not configured. Add it to a .env file or your environment."
        )

    return ollama.Client(
        host="https://ollama.com",
        headers={"Authorization": f"Bearer {api_key}"}
    )


def get_model():
    return os.getenv("OLLAMA_MODEL", "gpt-oss:20b")


def generate_dataset_insights(profile, recommendations):
    """
    Ask the LLM to explain the dataset profile
    and visualization recommendations.
    """

    prompt = f"""
You are an expert data analyst.

Analyze the following dataset information.

Dataset profile:
{json.dumps(profile, indent=2)}

Recommended visualizations:
{json.dumps(recommendations, indent=2)}

Provide:

1. A short dataset overview.
2. Important observations.
3. Which visualizations are most useful.
4. Potential data-quality concerns.
5. Suggestions for further analysis.

Keep the response concise and practical.
"""

    client = get_ollama_client()

    response = client.chat(
        model=get_model(),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def generate_chart_recommendation(df_info, user_question):

    prompt = f"""
You are an AI data visualization assistant.

Dataset information:

{df_info}

User request:

{user_question}

Determine:

1. Best chart type.
2. X-axis column.
3. Y-axis column.
4. Aggregation if necessary.
5. Short explanation.

Return ONLY valid JSON.

Example:

{{
    "chart_type": "scatter",
    "x": "Age",
    "y": "Salary",
    "aggregation": null,
    "reason": "A scatter plot is suitable for examining the relationship between age and salary."
}}
"""

    client = get_ollama_client()

    response = client.chat(
        model=get_model(),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    # Handle possible Markdown JSON response
    content = content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        return {
            "chart_type": None,
            "x": None,
            "y": None,
            "aggregation": None,
            "reason": content
        }


def explain_chart(chart_type, x, y):

    prompt = f"""
Explain this data visualization to a beginner.

Chart type: {chart_type}
X-axis: {x}
Y-axis: {y}

Explain:

- What the chart shows
- What the user should look for
- What a strong relationship would mean
- What an outlier could mean

Keep it under 150 words.
"""

    client = get_ollama_client()

    response = client.chat(
        model=get_model(),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]