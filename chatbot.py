from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from config import get_google_api_key

# 1. Connect to the Google Gemini API
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest", 
    google_api_key=get_google_api_key()
)

# 2. Setup the chatbot's "memory"
messages = [
    SystemMessage(content="You are a smart assistant for Engineer Mena in construction project management. Answer briefly and professionally.")
]

print("🤖 Chatbot is ready! (Type 'exit' to end the conversation)\n")
print("-" * 50)

# 3. Infinite loop
while True:
    user_input = input("Mena: ")
    
    if user_input.lower() == "exit":
        print("🤖 Goodbye, Engineer!")
        break

    messages.append(HumanMessage(content=user_input))
    
    # Send to AI
    response = llm.invoke(messages)

    # 4. Clean the output (Extract text only if it comes as a list)
    bot_reply = response.content
    if isinstance(bot_reply, list):
        bot_reply = bot_reply[0].get("text", "")

    # Print the clean response
    print("Bot:", bot_reply)
    print("-" * 50)

    # Save clean AI response to memory
    messages.append(AIMessage(content=bot_reply))