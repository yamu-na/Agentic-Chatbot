# 🤖 Agentic AI Chatbot

An AI-powered chatbot built using **LangGraph**, **LangChain**, **Groq LLM**, **Tavily Search API**, and **Streamlit**. The application demonstrates graph-based AI workflows with conversational AI, web search, and AI news summarization.

---

## 🚀 Features

- 💬 **Basic Chatbot** – General conversational AI powered by Groq LLM.
- 🌐 **Chatbot with Web** – Performs real-time web search using Tavily when required.
- 📰 **AI News** – Fetches and summarizes the latest AI news (Daily, Weekly, Monthly, Yearly).

---

## 🛠️ Tech Stack

- **Language:** Python
- **Frameworks:** LangGraph, LangChain, Streamlit
- **LLM:** Groq (Supports Llama 3.1 8B Instant, Llama 3.3 70B Versatile, and Gemma 2 9B IT)
- **APIs:** Groq API, Tavily Search API
- **Libraries:** LangChain Community, LangChain Core, FAISS

---

## 📂 Project Structure

```
Agentic-AI-Chatbot
│── app.py
│── requirements.txt
│── README.md
│── src/

```

---

## Installation

1. Clone the project

```bash
git clone <repository-url>
```

2. Navigate to the project

```bash
cd AgenticChatbot
```

3. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the application

```bash
streamlit run app.py
```
---

## 🔑 API Keys

This project requires:

- **Groq API Key** – https://console.groq.com/keys
- **Tavily API Key** – https://app.tavily.com/

Enter the keys through the Streamlit interface.

---
