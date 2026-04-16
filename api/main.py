from fastapi import FastAPI, UploadFile, File
import shutil
import os

from parser.document_parser import extract_text_from_pdf
from agent.claim_agent import ClaimAgent

app = FastAPI()
agent = ClaimAgent()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/process-claim")
async def process_claim(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    # Process using agent
    result = agent.process(text)

    return result