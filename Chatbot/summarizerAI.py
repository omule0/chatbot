# Import the required libraries
import openai
import streamlit as st

# Set the GPT-3 API key
# In this case, st.secrets["pass"] is accessing the value of the "pass" secret.

openai.api_key = st.secrets["api_secret"]

st.header("ChatBot")

article_text = st.text_area("Enter question")
temp = st.slider("temparature",0.0,1.0,0.5)

if len(article_text)>100:
    if st.button("Generate Summary"):
        response = openai.Completion.create(
        engine="davinci",
        prompt="please summarize this article for me in a few sentences "+article_text,
        temperature = temp,
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download Result", res)
else:
    st.warning("the sentence is not long enough")
     
     
import streamlit as st
import os

uploaded_file = st.file_uploader('File upload', type=['pdf'], accept_multiple_files=True)
