import os
from openai import OpenAI
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY')

client = OpenAI(api_key=SECRET_KEY)

res = client.chat.completions.create(
    model='gpt-4',
    messages= [
        {
            'role': 'user',
            'content': 'write a code for adding 2 nos'
        }
    ]
)

print("res is : ", res.choices[0].message.content)
# print("res is : ", res.choices[0].message.content)
