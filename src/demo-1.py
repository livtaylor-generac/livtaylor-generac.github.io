prompt="""Write a haiku about AC generators.
"""
openai_model="""gpt-4o
"""
from openai import OpenAI;
import json
print("prompt:", str(prompt))
client = OpenAI()
completion = client.chat.completions.create(
    model=openai_model.strip(),
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(completion)
print()
print("First Answer: ", completion.choices[0].message.content)
