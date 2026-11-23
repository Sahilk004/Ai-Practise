from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

st.title("Funny AI Chatbot")

# Keep the model and conversation history across Streamlit reruns
if "model" not in st.session_state:
    st.session_state.model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="You are a funny AI agent")]

# Display previous messages (skip the system message)
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
if prompt := st.chat_input("Enter your query"):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = st.session_state.model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)