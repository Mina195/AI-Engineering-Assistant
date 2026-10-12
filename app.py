import streamlit as st

from config import get_google_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

try:
    API_KEY = get_google_api_key()
except RuntimeError as error:
    st.error(str(error))
    st.stop()

st.set_page_config(page_title="Engineering Assistant", page_icon="🏗️")
st.title("🏗️ AI Engineering Assistant")
st.caption("Powered by LangChain & Google Gemini - Built by Eng. Mena")

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", google_api_key=API_KEY)

# Store conversation history in Streamlit session state between reruns.
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a smart assistant for Engineer Mena in construction project management. Answer briefly and professionally.")
    ]

# Display the conversation history, excluding the system message.
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

if prompt := st.chat_input("Ask me anything about engineering..."):
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.messages)

            bot_reply = response.content
            if isinstance(bot_reply, list):
                bot_reply = bot_reply[0].get("text", "")

            st.write(bot_reply)

    st.session_state.messages.append(AIMessage(content=bot_reply))