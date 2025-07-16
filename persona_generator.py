import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(text_corpus):
    prompt = f"""
You are an AI trained to generate user personas based on Reddit activity.

Based on the following Reddit posts and comments, generate a detailed user persona that includes:
- Personality Traits
- Interests
- Motivations
- Behavior & Habits
- Frustrations
- Goals & Needs

For each trait, cite a relevant post/comment. Format:
Trait: <description>
Source: <post or comment snippet with link>

--- USER DATA START ---
{text_corpus}
--- USER DATA END ---
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
