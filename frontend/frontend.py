import streamlit as st
from langchain_ollama import OllamaLLM

st.title("Local AI Assistant (Ollama)")
st.write("Running 100% on localhost")

llm = OllamaLLM(model="llama3")

user_question = st.text_input("Ask a question:")

if user_question:
    with st.spinner("Thinking..."):
        response = llm.invoke(user_question)

    st.subheader("Answer")
    st.write(response)