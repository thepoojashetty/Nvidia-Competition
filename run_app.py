import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
import time

api_key = os.environ.get("NVIDIA_API_KEY")
llm = ChatNVIDIA(model="mistralai/mixtral-8x7b-instruct-v0.1", api_key=api_key)

def get_completion(prompt):
    result = llm.invoke(prompt)
    return result.content

st.title("NVIDIA Language Model Chat")

# with st.form('my_form'):
#     text = st.text_area('Ask me anything')

#     submitted = st.form_submit_button('Submit')
#     if submitted:
#         get_completion(text)
# st.text_input("Your name", key="name")

if "messages" not in st.session_state:
    st.session_state.messages = []

#role could be user or assistant
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_completion(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})