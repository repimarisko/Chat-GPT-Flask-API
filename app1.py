import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
a = input("Masukan text : ")
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=a,
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)
print(response.choices[0].text)
