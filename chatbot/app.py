import streamlit as st

# Initialize session state variables if not already initialized
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def get_faq_response(question):
    # Dummy function for chatbot response
    faq_responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm a bot, but I'm here to help!",
        "what is streamlit": "Streamlit is an open-source app framework for Machine Learning and Data Science teams.",
    }
    return faq_responses.get(question.lower(), "Sorry, I don't have an answer to that question.")

def handle_user_input():
    user_question = st.session_state.user_input
    if user_question:
        response = get_faq_response(user_question)
        st.session_state.chat_history.append((user_question, response))
        st.session_state.user_input = ''  # Clear input field

# Set the page title and layout
st.set_page_config(page_title="Simple FAQ Chatbot", layout="centered")

# Title of the app
st.title("Simple FAQ Chatbot")

# Display chat history
for question, answer in st.session_state.chat_history:
    st.write(f"You: {question}")
    st.write(f"Bot: {answer}")

# Input form for user questions
st.text_input("You:", key='user_input', on_change=handle_user_input)

# Button to clear chat history
if st.button("Clear Chat"):
    st.session_state.chat_history = []
