import os
from google import genai
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(dotenv_path)
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY1')
client = genai.Client(api_key=SECRET_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)