import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print("OpenAI Chat GPT Prompt> ", end='')
p = input()

print("Your prompt is: \n<", p, ">\n", sep='')

response = openai.Completion.create(
            model="text-davinci-003",
            prompt=p,
            temperature=0.6,
        )

if (response.object == "text_completion"):
    for c in response.choices:
        print("ChatGPT Response:", c.text)
