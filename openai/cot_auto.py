import os, json
from openai import OpenAI
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY')

client = OpenAI(api_key=SECRET_KEY)

system_prompt = """

you are an AI assistant who is having good knowledge about tech and coding.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: write a code to create dataframe in pandas.
Output: {{ step: "analyse", content: "Alright! The user is intersted in coding and he is asking a to create pandas dataframe" }}
Output: {{ step: "think", content: "To create dataframe code I must think properly before writing code" }}
Output: {{ step: "output", content: "writing code in pandas to create dataframe" }}
Output: {{ step: "validate", content: "this is the solution to create dataframe" }}
Output: {{ step: "result", content: "above code is written in pandas" }}

"""

messages = [
    {"role": "system", "content": system_prompt}
]

query = input(">")
messages.append({"role": "user", "content": query})

while True:
    res = client.chat.completions.create(
        model='gpt-4o',
        response_format={"type": "json_object"},
        messages=messages
    )

    parsed_response = json.loads(res.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_response)})

    if parsed_response.get("step") != "output":
        print(f"Thinking: {parsed_response.get("content")}")
        continue

    print(f"The ans is: {parsed_response.get("content")}")
    break


