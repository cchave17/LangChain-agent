import os
from apikey import apikey

import streamlit as st 
from langchain.llms import OpenAI


os.environ['OPENAI_API_KEY'] = apikey

# App Framework 
st.title('🦜🔗 Tutor GPT')
prompt = st.text_input('Plug in your prompt here') 


# llms
llm = OpenAI(temperature=0.9)

# Display response if prompted
if prompt:
    response = llm(prompt)
    st.write(response)
