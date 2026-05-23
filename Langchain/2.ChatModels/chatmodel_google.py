from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash-lite')

response = model.invoke("What is the capital of india?")
print(response.content)

# client = genai.Client()
# for m in client.models.list():
#     if "generateContent" in m.supported_actions:
#         print(m.name)
