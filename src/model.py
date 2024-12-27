import streamlit as st
from llama_index.core.llms import ChatMessage
from llama_index.llms.ollama import Ollama
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import logging
import time

logging.basicConfig(level=logging.INFO)

# Initialize embeddings
local_embeddings = OllamaEmbeddings(model="all-minilm")

# Initialize Chroma with an embedding function
chroma_store = Chroma(collection_name="chat_collection", embedding_function=local_embeddings.embed_query)

if 'messages' not in st.session_state:
    st.session_state.messages = []

def stream_chat(model, messages):
    try:
        llm = Ollama(model=model, request_timeout=120.0)
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        logging.info(f"Model: {model}, Messages: {messages}, Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error during streaming: {str(e)}")
        return None  # Return None instead of raising an exception

def save_to_vector_store(user_query, assistant_response):
    # Create documents from user query and assistant response
    user_doc = {"content": user_query}
    assistant_doc = {"content": assistant_response}
    
    # Add documents to the vector store
    try:
        chroma_store.add_documents([user_doc, assistant_doc])
    except Exception as e:
        logging.error(f"Error saving to vector store: {str(e)}")

def main():
    st.title("Chat with LLMs Models")
    logging.info("App started")

    model = st.sidebar.selectbox("Choose a model", ["llama3.2:latest", "llama3.1 8b", "phi3", "mistral"])
    logging.info(f"Model selected: {model}")

    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        logging.info(f"User input: {prompt}")

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                start_time = time.time()
                logging.info("Generating response")

                with st.spinner("Writing..."):
                    try:
                        messages = [ChatMessage(role=msg["role"], content=msg["content"]) for msg in st.session_state.messages]
                        response_message = stream_chat(model, messages)

                        if response_message is None:
                            raise Exception("Failed to generate a response.")

                        duration = time.time() - start_time
                        response_message_with_duration = f"{response_message}\n\nDuration: {duration:.2f} seconds"
                        
                        # Save user query and assistant response to the vector store
                        save_to_vector_store(prompt, response_message)

                        st.session_state.messages.append({"role": "assistant", "content": response_message_with_duration})
                        st.write(f"Duration: {duration:.2f} seconds")
                        logging.info(f"Response: {response_message}, Duration: {duration:.2f} s")

                    except Exception as e:
                        st.session_state.messages.append({"role": "assistant", "content": "An error occurred while generating the response."})
                        st.error("An unexpected error occurred. Please try again later.")
                        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()