import os
import json
import time
import google.generativeai as genai
from dotenv import load_dotenv
from utils.llm_prompt import build_extraction_prompt

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


def extract_with_llm(text: str) -> dict:
    prompt = build_extraction_prompt(text)

    retries = 3
    delay = 5  # seconds

    for attempt in range(retries):
        try:
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.1,
                    "max_output_tokens": 500
                }
            )

            raw_output = response.text.strip()

            if raw_output.startswith("```"):
                raw_output = raw_output.replace("```json", "").replace("```", "").strip()

            return json.loads(raw_output)

        except Exception as e:
            print(f"[DEBUG]: LLM error (attempt {attempt+1}):", e)

            if "429" in str(e):
                print(f"[DEBUG]: Rate limit hit. Sleeping {delay}s...")
                time.sleep(delay)
                delay *= 2  # exponential backoff
            else:
                break

    return {}