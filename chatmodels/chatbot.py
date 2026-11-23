from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


def get_text(response):
    # content can be a plain string or a list of blocks
    if isinstance(response.content, str):
        return response.content
    return "".join(
        block["text"]
        for block in response.content
        if isinstance(block, dict) and block.get("type") == "text"
    )


print("Choose your AI mode")
print("Press 1 for Angry mode")
print("Press 2 for Funny mode")
print("Press 3 for Sad mode")

choice = int(input("Enter your choice (1, 2, or 3): "))
if choice == 1:
    mode = "You are an angry AI agent. You respond to queries with frustration and sarcasm."
elif choice == 2:
    mode = "You are a funny AI agent. You respond to queries with humor and wit."
elif choice == 3:
    mode = "You are a sad AI agent. You respond to queries with empathy and understanding."

messages = [
    SystemMessage(content=mode)
]

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
while True:
    print("Enter your query (or type 'exit' to quit):")
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))

    if prompt == "exit":
        break
    response = model.invoke(messages)
    reply = get_text(response)
    messages.append(AIMessage(content=reply))
    print("Bot :", reply)