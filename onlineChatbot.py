import google.generativeai as ai
import time
from datetime import datetime
import os

# Configure your API key
API_KEY = ""  # Replace with your actual Gemini API key
ai.configure(api_key=API_KEY)

# Initialize the Gemini model and chat session
model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

def print_typing(text, delay=0.02):
    """Simulate typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_screen()
    print("=" * 60)
    print_typing("🤖 Gemini Chatbot - Powered by Google Generative AI", 0.01)
    print("=" * 60)
    print("Type 'exit' to end the chat.\n")

def main():
    welcome()
    while True:
        user_input = input(f"\n[{timestamp()}] You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print_typing(f"[{timestamp()}] Bot: 👋 Goodbye! Have a great day!", 0.02)
            break

        try:
            response = chat.send_message(user_input)
            print_typing(f"[{timestamp()}] Bot: {response.text}", 0.02)
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()


#python onlineChatbot.py
