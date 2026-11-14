from google import genai
from dotenv import load_dotenv
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Load Env
load_dotenv()

#Load genai
genClient = genai.Client()

#Read File
with open("rag_spring_boot_knowledge_base.txt", "r", encoding="utf-8") as file:
    text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=20,
    separators=["\n"]
)

chunks = splitter.split_text(text)

#Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(name="rag")


collection.upsert(
    documents=chunks,
    ids=[f"chunk-{i} "for i in range(len(chunks))]
)


question = "Which framework is used to develop microservices?"

#Fetch Chunks
contextInfo = collection.query(
    query_texts=[question],
    n_results=2
)

print("Context is")
print(contextInfo.get("documents")[0])

contents=f"""
        Context is:
        {contextInfo.get("documents")[0]}

        Question is: {question}
    """

print("Content is") 
print(contents)

response = genClient.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents
)
print("Response is ")
print(response.text)

