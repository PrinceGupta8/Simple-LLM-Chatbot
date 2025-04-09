# 💭 Dream – Generative AI Chatbot

Dream is a lightweight, local-first chatbot powered by the **Gemma 2B** large language model via **Ollama**, built using **LangChain** and **Streamlit**. It’s designed to help users generate intelligent and creative responses, fully offline.

## 🚀 Features
- 🌐 Built with **Streamlit** for a seamless UI
- ⚡ Uses **LangChain** prompt chains and output parsing
- 🧠 Powered by **Ollama's local Gemma 2B model**
- 🔒 Secure environment with `.env` file integration
- 🧱 Modular, extensible architecture

## 🧰 Tech Stack
- Python 3.9+
- LangChain
- Ollama
- Streamlit
- dotenv

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/PrinceGupta8/Simple-LLM-Chatbot.git
cd Simple-LLM-Chatbot
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Install and Run Ollama
Install Ollama and pull the `gemma:2b` model:
```bash
ollama run gemma:2b
```

### 4. Setup Environment Variables
Create a `.env` file using the sample:
```bash
cp .env.example .env
```
And add your environment variables as needed.

### 5. Run the App
```bash
streamlit run chatbot.py
```

---

## 🧠 Credits
Thanks to:
- LangChain for the powerful chaining tools
- Ollama for local LLM support
- Streamlit for rapid prototyping
