# Utils/Agents.py

from groq import Groq
import os


class GroqAgent:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        key_path = os.path.join(project_root, "apikey.txt")

        if not os.path.exists(key_path):
            raise RuntimeError("apikey.txt not found in test-ai folder")

        with open(key_path, "r", encoding="utf-8") as f:
            api_key = f.read().strip().replace("\ufeff", "")

        if not api_key.startswith("gsk_"):
            raise RuntimeError("Invalid Groq API key")

        print("✅ Groq key loaded:", api_key[:8] + "..." + api_key[-4:])

        # ✅ OFFICIAL GROQ CLIENT
        self.client = Groq(api_key=api_key)

    def ask(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=512
        )
        return response.choices[0].message.content