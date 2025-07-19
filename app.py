import streamlit as st
from Chat_Bot.Function_app import get_response
from langchain_core.messages import AIMessage, HumanMessage


st.title("AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show messages 
for mes in st.session_state.chat_history:
    if isinstance(mes, AIMessage):
        with st.chat_message("AI"):
            st.write(mes.content)
    elif isinstance(mes, HumanMessage):
        with st.chat_message("Human"):
            st.write(mes.content)


user_input = st.chat_input("Type Your message here...")

if user_input is not None and user_input != "":
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("Human"):
        st.markdown(user_input)

    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_input, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))