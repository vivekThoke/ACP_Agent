import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from utils.llm_prompt import build_extraction_prompt

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


def extract_with_llm(text: str) -> dict:
    prompt = build_extraction_prompt(text)

    try:
        response = model.generate_content(prompt)

        raw_output = response.text.strip()

        if raw_output.startswith("```"):
            raw_output = raw_output.replace("```json", "").replace("```", "").strip()

        data = json.loads(raw_output)

        return data

    except Exception as e:
        print("[DEBUG]: LLM extraction failed:", e)
        return {}