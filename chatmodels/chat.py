from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# model = init_chat_model("google_genai:gemini-3.7-flash")

# response = model.invoke("What is cricket?")

# print(response.content)

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash",temperature=0)

response = model.invoke("Write a Poem on AI")

print(response.content)