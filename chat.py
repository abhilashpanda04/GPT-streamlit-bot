import streamlit as st
import streamlit_chat as sc
from dotenv import load_dotenv
from utils import get_initial_message,bot_reponse,update_chat
import openai
import os



def on_btn_click():
    """
    Clears the session state when the button is clicked.
    """
    del st.session_state.messages[:]
    del st.session_state.past[:]
    del st.session_state.generated[:]

def handle_query(query):
    
    if "generated" not in st.session_state:
        st.session_state.generated=[]
    if 'past' not in st.session_state:
        st.session_state.past=[]

    if "messages" not in st.session_state:
        st.write('initiating general prompt')
        st.session_state['messages'] = get_initial_message()

    if query:
        with st.spinner('Thinking...'):
            messages=st.session_state['messages']
            messages=update_chat(messages,"user",query)
            response=bot_reponse(messages)
            messages=update_chat(messages,"assistant",response)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1,-1,-1):#reversing the array to display correctly
            sc.message(st.session_state['past'][i],is_user=True,key=f'{str(i)}_user')#mentioning this is user
            sc.message(st.session_state['generated'][i],key=str(i))#mention this is bot
        with st.expander("Show Messages"):
            st.write(messages)#acummulated the messages
        clear_chat=st.button("Clear message", on_click=on_btn_click)


if __name__=='__main__':
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    st.title("Chatbot Streamlit")
    query=st.text_input("Your Question here: ",key="input",)
    if query:
        handle_query(query) 
    

