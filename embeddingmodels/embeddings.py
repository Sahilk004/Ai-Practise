from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions = 64
)

texts = [
    "Machine learning enables computers to learn from data.",
    "Deep learning uses neural networks to solve complex problems.",
    "I am learning Generative AI and building projects with LLMs."
]

#embed_documents = pure document ke liye
#embed_query = ek line ke liye
vector = embeddings.embed_documents(texts)
print(vector)