import os
from openai import OpenAI
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY')

client = OpenAI(api_key=SECRET_KEY)

system_prompt = """
You are an AI Assistant who is good in maths.
You should not answer any query which is not related to maths.

For a given query help user to solve with explanation.

Example:
Input: 2 + 2
Output: 2 + 2 is 4 which is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by multipling 3 by 10. Funfact you can even multiply 10 * 3 which gives same result.

Input: Why is sky blue?
Output: Bruh? Have you lost your mind? Is it maths query from any angle?

"""

res = client.chat.completions.create(
    model='gpt-4',
    messages=[
        {'role': "system", "content": system_prompt},
        {'role': "user", "content": "What is protons?"},
    ]

)

print("res is : ", res.choices[0].message.content)