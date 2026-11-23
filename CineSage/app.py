
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an intelligent information extraction assistant.

        Your task is to extract useful information from the
        given text and return it in a structured JSON format.

        Extract the following fields whenever applicable:

        1. Movie name
        2. Release year
        3. Director
        4. Writers
        5. Cast members and their character names
        6. Genres
        7. Language
        8. Country of origin
        9. Main characters
        10. Plot
        11. Central conflict
        12. IMDb rating
        13. Awards and achievements
        14. Critical and audience reception
        15. Themes and unique features
        16. Keywords (5-10 relevant keywords)
        17. Summary (2-3 concise sentences)

        Rules:
        - Extract only information supported by the input text.
        - Never invent missing information.
        - Use null for missing single-value fields.
        - Use empty lists for missing list fields.
        - Represent cast members as objects containing actor
          and character fields.
        - Keep the summary concise and informative.
        - Return valid JSON only.
        - Do not include Markdown or additional explanations.
        """
    ),
    (
        "human",
        """
        Extract useful information from the following text:

        {text}
        """
    )
])

st.title("Movie Information Extraction")

para = st.text_area("Enter your movie paragraph:")

if st.button("Extract Information"):
    if para.strip():
        final_prompt = prompt.invoke({"text": para})
        response = model.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.code(response.content, language="json")
