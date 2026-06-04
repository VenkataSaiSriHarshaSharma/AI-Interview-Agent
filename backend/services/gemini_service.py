from openai import OpenAI
import os

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_content(prompt):

    response = client.chat.completions.create(

        model="nvidia/nemotron-3-ultra-550b-a55b:free",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=4000

    )

    return response.choices[0].message.content


# compatibility for old imports
model = None