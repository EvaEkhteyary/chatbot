from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question):
    
    response = client.models.generate_content(
    model="type your model here", #if you have a model, type it here
    contents=question
    )
    return response.text

## initialise our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("chatbot")

# initialise session state for chat history if it doesnt exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input =st.text_input("input:",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is")
    #for chunk in response:
    st.write(response)
    st.session_state['chat_history'].append(("Bot",response))
st.subheader("The Chat History is")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")      

