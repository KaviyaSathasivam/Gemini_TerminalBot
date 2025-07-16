# 🤖 Gemini Chatbot - Powered by Google Generative AI

This is a simple terminal-based chatbot built using the **Google Generative AI (Gemini)** API. The chatbot simulates a conversation with a typing effect and logs timestamps for user and bot messages.

## 📦 Features

- ✅ Real-time chatbot powered by Gemini 1.5 Flash model
- ✅ Typing effect for a realistic conversation feel
- ✅ Timestamp for every message
- ✅ Clean and minimal command-line interface
- ✅ Graceful exit commands (`exit`, `quit`, `bye`)

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot

**2. Install Required Dependencies**
Make sure you have Python 3.7+ installed. Then install the required package:
pip install google-generativeai

**3. Set Up Your API Key**
Get your API key from: https://makersuite.google.com/app/apikey

Open onlineChatbot.py and replace this line:
API_KEY = ""  # Replace with your actual Gemini API key
with:
API_KEY = "your-api-key-here"

**4. Run the Chatbot**
python onlineChatbot.py

🛑 Exit the Chat
To exit the chatbot at any time, simply type:

exit
or
quit
or
bye


📁 Project Structure

gemini-chatbot/
│
├── onlineChatbot.py   # Main Python script for the chatbot
├── README.md          # Project documentation
🧠 Powered By
Google Generative AI (Gemini)
Python Standard Libraries: time, datetime, os
