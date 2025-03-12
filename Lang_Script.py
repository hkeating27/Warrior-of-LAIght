from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
#import os
#os.environ["OPENAI_API_KEY"] = "example"


# Load and split FFXIV job guide into vector database
def load_knowledge_base(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    return docs

# Create FAISS vector database for retrieving FFXIV job information
def create_vector_db(docs):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store

# Initialize AI assistant for FFXIV job selection
def setup_ai_assistant():
    docs = load_knowledge_base("ffxiv_job_guide.txt")  # Using the guide as knowledge base
    vector_store = create_vector_db(docs)
    
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    
    return conversational_chain

if __name__ == "__main__":
    assistant = setup_ai_assistant()
    print("FFXIV Job Guide Assistant is ready. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = assistant.invoke({"question": user_input})
        print("AI:", response["answer"])
