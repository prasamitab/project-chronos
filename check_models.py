import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads your .env file
genai.configure(api_key=os.getenv("AIzaSyBISXh-4QFcNuHj99eeMS7Rz6KQ5AuUNfs"))

print("🔍 Available Gemini Models:")
for m in genai.list_models():
    print("-", m.name)

