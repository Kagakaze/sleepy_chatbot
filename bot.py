from openai import OpenAI
import os

client = OpenAI()

response = client.responses.create(
  model="gpt-5-nano",
  input=input("envoyer un message a gpt : "),
  store=True,
)

print(response.output_text)