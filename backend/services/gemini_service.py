from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_content(prompt):
    try:

        response = client.chat.completions.create(

            model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert AI Recruitment Assistant.

Your responsibilities:
1. Analyze resumes professionally.
2. Generate technical interview questions.
3. Evaluate candidate answers.
4. Generate detailed hiring recommendations.
5. Provide structured reports.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,
            max_tokens=2000

        )

        print("\n========== OPENROUTER RESPONSE ==========")
        print(response)
        print("=========================================\n")

        if response is None:
            return "Response is None"

        if not hasattr(response, "choices"):
            return f"Invalid response:\n{response}"

        if response.choices is None:
            return f"No choices returned.\nFull Response:\n{response}"

        if len(response.choices) == 0:
            return f"No choices returned.\nFull Response:\n{response}"

        message = response.choices[0].message

        if message is None:
            return f"No message returned.\nFull Response:\n{response}"

        content = message.content

        if not content:
            return f"Empty content returned.\nFull Response:\n{response}"

        print("\n========== GENERATED CONTENT ==========")
        print(content)
        print("=======================================\n")

        return content

    except Exception as e:

        print("\n========== OPENROUTER ERROR ==========")
        print(str(e))
        print("======================================\n")

        return f"OpenRouter Error:\n{str(e)}"