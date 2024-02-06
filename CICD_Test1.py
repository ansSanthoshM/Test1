# pip install streamlit
# pip install streamlit_extras.stylable_container
# pip install langchain

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)


st.set_page_config(page_title="Llama2 TGI Streaming ",layout="wide",)
st.title ("Llama2 TGI Streaming Test 1")

with stylable_container(
    key="top_content",
    css_styles="""
    {
        position: fixed;
        top: 0px;
        right: 100px;
        width :100px;
        color: #D69D3C;
        margin:100px 0px 10rem;
        background-color: #0E1117;
    }""",
    ):
    clear_button = st.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            AIMessage(content= "Welcome! How can I assist you today? ?")
                ]
        
def llm():
    return "Response from LLM"
        
# Display chat history
messages = st.session_state.get("messages", [])  
for message in messages:  
    if isinstance(message, AIMessage):  
        with st.chat_message("assistant", avatar='🦙'):  
            st.markdown(message.content)  
    elif isinstance(message, HumanMessage):  
        with st.chat_message("user",avatar='👩‍🎨'):  
            st.markdown(message.content)
            
#Main function
if __name__ == '__main__':

    if user_question := st.chat_input("Input your technical question!, Please note my current capablity is limited to completion model"):
        st.session_state.messages.append(HumanMessage(content=user_question))
        with st.chat_message("user",avatar='👩‍🎨'):  
            st.markdown(user_question)
        with st.chat_message("assistant",avatar='🦙'):
            response = llm()
            st.session_state.messages.append(AIMessage(content=response))


    
