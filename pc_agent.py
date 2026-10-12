import os
import streamlit as st
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from config import get_google_api_key

# 1. Page Configuration (The UI settings)
st.set_page_config(page_title="Windows AI Agent", page_icon="💻")
st.title("💻 Windows AI Agent")
st.caption("Control your PC using natural language - Built by Eng. Mena")

# 2. The Tool (The "hands" that will control your laptop)
@tool
def open_program(program_name: str) -> str:
    """
    Use this tool ONLY when the user asks to open, launch, or start a program on the computer.
    The input must be the executable name of the program, such as: 'calc' for calculator, 'acad' for AutoCAD, or 'notepad'.
    """
    os.system(f"start {program_name}")
    return f"Program {program_name} opened successfully."

# 3. Setup the Brain and bind it to the tools
API_KEY = get_google_api_key()
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", google_api_key=API_KEY)
llm_with_tools = llm.bind_tools([open_program])
tools_map = {"open_program": open_program}

# 4. Session State for Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation history on the screen
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# 5. Chat Input (The message box at the bottom)
if user_input := st.chat_input("Type a command (e.g., Open Calculator)..."):
    
    # Print user's command on the screen and save to memory
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append(HumanMessage(content=user_input))

    # AI Processing with a loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Executing your command..."):
            
            # Send the request to the AI
            response = llm_with_tools.invoke([HumanMessage(content=user_input)])

            # 6. Check: Did the AI decide to use a tool? (Function Calling)
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    name = tool_call["name"]
                    args = tool_call["args"]
                    
                    if name in tools_map:
                        # Execute the tool on Windows
                        tools_map[name].invoke(args)
                        
                        # Show a success message in the chat
                        program = args.get('program_name', 'the program')
                        success_msg = f"✅ Executed Windows command: Opened {program} successfully!"
                        st.write(success_msg)
                        
                        # Save the success message to memory
                        st.session_state.messages.append(AIMessage(content=success_msg))
            else:
                # CLEAN THE OUTPUT: If no tool was used, just reply normally
                bot_reply = response.content
                if isinstance(bot_reply, list):
                    bot_reply = bot_reply[0].get("text", "")
                
                st.write(bot_reply)
                st.session_state.messages.append(AIMessage(content=bot_reply))