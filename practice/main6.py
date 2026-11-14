from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

text = """
Java is an object-oriented programming language.

Spring Boot is a Java framework used to build microservices.

Python is widely used in artificial intelligence.

RAG combines document retrieval with large language models.

I love microservices.
"""

splitter = RecursiveCharacterTextSplitter (
    chunk_size=10,
    chunk_overlap=10,
    separators=['\n']
)

chunks = splitter.split_text(text)

# Step 3: Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Step 4: Create or retrieve a collection
collection = client.get_or_create_collection(
    name="my_documents"
)

# Step 5: Store the chunks
collection.upsert(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print("Total stored chunks:", collection.count())

# Step 6: Search the vector database
question = "Which framework is used to develop microservices?"

results = collection.query(
    query_texts=[question],
    n_results=2
)

# Step 7: Print retrieved chunks
# for document in results["documents"][0]:
#     print("Retrieved:", document)

##print(results["documents"])

# print(type(collection))

# results = collection.get()
# print(results)

results = collection.get(
    include=["documents", "embeddings", "metadatas"]
)

print(results)

# for i, doc_id in enumerate(results["ids"]):
#     print("ID:", doc_id) 
#     print("Document:", results["documents"][i])
#     print("Embedding:", results["embeddings"][i])
#     print("--------------------------")