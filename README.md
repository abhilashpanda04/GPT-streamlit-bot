# GPT-streamlit-bot

This is a Streamlit app that implements a chatbot using the streamlit and streamlit_chat libraries. The chatbot uses the OpenAI API for generating responses.

Installation
To run the chatbot, you need to install the required dependencies. You can use pip to install them:

```
pip install streamlit streamlit_chat python-dotenv openai
```
# Usage
# Import the necessary modules:
```
import streamlit as st
import streamlit_chat as sc
from dotenv import load_dotenv
from utils import get_initial_message, bot_response, update_chat
import openai
import os
Load the environment variables (API key):
```
```
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```
# Set up the Streamlit app:
```
st.title("Chatbot Streamlit")

if "generated" not in st.session_state:
    st.session_state.generated = []
if "past" not in st.session_state:
    st.session_state.past = []

query = st.text_input("Your Question here: ", key="input")

if "message" not in st.session_state:
    st.session_state.message = get_initial_message()

if query:
    with st.spinner('Thinking...'):
        messages = st.session_state.message
        messages = update_chat(messages, "user", query)
        response = bot_response(messages)
        messages = update_chat(messages, "assistant", query)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

```

# Display the chat history:
```
if st.session_state.generated:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        sc.message(st.session_state['past'][i], is_user=True, key=f'{str(i)}_user')
        sc.message(st.session_state['generated'][i], key=str(i))
```

# Additional Notes

- The streamlit library is used to create the Streamlit app and handle user input.
- The streamlit_chat library provides the UI components for displaying chat messages.
- The dotenv library is used to load environment variables from a .env file.
- The get_initial_message function retrieves the initial message to start the conversation.
- The bot_response function sends the user's query to the OpenAI API and generates a response.
- The update_chat function updates the chat history with the user's query and the bot's response.
- The chat history is stored in the Streamlit session state to maintain state between user interactions.
- Feel free to modify the code and customize it according to your needs. Happy chatting!


