# from openai import OpenAI
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

for model in client.models.list():
    if model.supported_actions and "generateContent" in model.supported_actions:
        print(model.name)


# Generate response
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain RAG in one sentence."
)

print(response.text)