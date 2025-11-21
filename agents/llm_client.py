# agents/llm_client.py
import os
import google.generativeai as genai

class GoogleClient:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def call(self, prompt: str, **kwargs) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"ERROR_CALLING_GOOGLE: {e}"

def get_llm_client():
    return GoogleClient()