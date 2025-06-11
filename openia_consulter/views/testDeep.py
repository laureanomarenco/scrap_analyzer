    
from openai import OpenAI

def testDeep():
    client = OpenAI(api_key="sk-78aff42bc40d4c08bfd57f4bd7331890", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)