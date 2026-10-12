# AI Engineering Assistant & Windows AI Agent

An AI-powered engineering assistant built with Python, LangChain, Google Gemini, and Streamlit. The project explores how large language models can support engineering-related conversations and interact with local computer applications through tool calling.

## Project Overview

This project explores practical applications of generative AI through conversational interfaces, context-aware responses, and AI-driven tool execution.

It includes a web-based engineering assistant, a command-line chatbot, and a Windows AI agent capable of launching permitted desktop applications.

## Features

### 1. AI Engineering Assistant

* Interactive chat interface built with Streamlit.
* Integration with Google Gemini through LangChain.
* Conversation history maintained using Streamlit session state.
* System instructions tailored to engineering and construction project management.
* Natural-language interaction with the AI model.

### 2. Windows AI Agent

* Natural-language interface for requesting desktop actions.
* Integration of LangChain tool calling with a Python function for launching Windows applications.
* AI-generated tool calls handled by application logic.
* Streamlit-based chat interface.

**Security note:** Desktop actions should be restricted to explicitly permitted applications. Never execute arbitrary model-generated shell commands.

### 3. Command-Line Chatbot

* Terminal-based conversational interface.
* Conversation history maintained during the session.
* Gemini integration through LangChain.
* Graceful conversation termination.

### 4. API Utility Scripts

* `list_models.py`: Retrieves available Gemini models and filters for text-generation support.
* `test_api.py`: Tests connectivity to the Gemini API.

## Technology Stack

* **Python** — Core application logic.
* **Streamlit** — Interactive web interface.
* **LangChain** — LLM integration, message handling, and tool calling.
* **Google Gemini API** — Language-model capabilities.
* **Requests** — HTTP requests for API testing and model discovery.
* **python-dotenv** — Local environment-variable configuration.

## Project Structure

```text
AI-Engineering-Assistant/
├── app.py
├── chatbot.py
├── pc_agent.py
├── list_models.py
├── test_api.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

## Getting Started

### Prerequisites

* Python 3.10 or a compatible version supported by the installed dependencies.
* A Google Gemini API key.
* Git, if you want to clone the repository.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Engineering-Assistant.git
cd AI-Engineering-Assistant
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

Activate it using Command Prompt:

```bat
.venv\Scripts\activate
```

Or, if you are using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your API key

Create a local `.env` file in the project root:

```dotenv
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Replace the placeholder with your own API key.

**Never commit your `.env` file or expose your API key in source code.**

### 5. Run the Engineering Assistant

```bash
streamlit run app.py
```

Streamlit will provide a local address where you can open the application in your browser.

### 6. Run the Windows AI Agent

```bash
streamlit run pc_agent.py
```

Use this application only with the intended Windows environment and an explicitly restricted set of permitted programs.

### 7. Run the command-line chatbot

```bash
python chatbot.py
```

### 8. Run the API utilities

```bash
python list_models.py
```

```bash
python test_api.py
```

These utility scripts require valid API configuration and compatible model identifiers.

## Configuration

The applications use the `GOOGLE_API_KEY` environment variable to authenticate with the Gemini API.

Model availability and supported identifiers may change. Configure a model that is available to your account and supported by your installed LangChain integration.

## Current Scope and Limitations

* The Engineering Assistant focuses on conversational engineering support; it is not a substitute for professional engineering review.
* Conversation history is maintained within the application's session and is not a persistent database.
* The Windows agent currently focuses on launching desktop applications rather than providing unrestricted computer control.
* The project requires a valid Gemini API key and an internet connection.
* Application behavior depends on the configured model and installed dependency versions.

## Future Improvements

* Add structured configuration and error handling.
* Introduce automated tests for core functionality.
* Improve desktop-agent security and application allowlisting.
* Add screenshots and demonstrations of the applications.
* Improve conversation-memory management.
* Add deployment instructions for a hosted version of the web application.

## Author

**Mena Nady**

Construction Engineering graduate with an interest in AI, automation, and practical applications of large language models.

This project represents hands-on exploration of Python application development, LLM integration, conversational interfaces, and AI tool calling.
