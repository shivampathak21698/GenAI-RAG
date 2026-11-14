from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
Hue.
Java is a programming language.
Spring Boot is used to build microservices.
Python is widely used in artificial intelligence.
RAG combines document retrieval with LLMs.
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=10,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)

print(chunks)