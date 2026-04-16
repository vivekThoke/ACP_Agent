# 🚀 Autonomous Insurance Claims Processing Agent

## 📌 Overview

This project is an **end-to-end AI-powered system** that processes **FNOL (First Notice of Loss) documents** such as insurance claim forms.

It allows users to:

* Upload FNOL documents (PDF/TXT)
* Automatically extract key insurance fields
* Detect missing or inconsistent data
* Classify and route the claim
* View results in both **JSON format** and a **structured UI**

---

## 🧠 What This Project Does

The system acts as an **Autonomous AI Agent** that:

### ✅ Extracts Information

From FNOL documents:

* Policy Number
* Policyholder Name
* Incident Date
* Description
* Estimated Damage

### ⚠️ Detects Missing Fields

Identifies incomplete claims automatically.

### 🔀 Routes Claims

Based on business rules:

* Low damage → Fast Track
* Missing data → Manual Review
* Fraud keywords → Investigation
* Injury → Specialist Queue

### 🧾 Explains Decisions

Provides reasoning for why a claim was routed a certain way.

---

## 🏗️ Architecture

```text
Frontend (React)
      ↓
FastAPI Backend (Python)
      ↓
Autonomous Agent
      ↓
[Parser → Extractor → Validator → Router]
```

---

## 📁 Project Structure

```bash
insurance-claims-agent/
│
├── backend/
│   ├── api/main.py              # FastAPI entry point
│   ├── agent/claim_agent.py     # Autonomous agent logic
│   ├── parser/                 # PDF/TXT parsing
│   ├── extractor/              # Regex + LLM extraction
│   ├── validator/              # Missing field detection
│   ├── router/                 # Business rules
│   ├── utils/                  # Prompts, cache, helpers
│   └── temp/                   # Uploaded files
│
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── components/
    │   └── services/
```

---

## ⚙️ How It Works (Step-by-Step)

### 1️⃣ Document Upload

User uploads a PDF/TXT file from the frontend.

### 2️⃣ Text Extraction

* PDFs → processed using `pdfplumber`
* TXT → read directly

### 3️⃣ Field Extraction

Hybrid approach:

* ✅ Regex (fast, deterministic)
* 🧠 LLM (Gemini) fallback for complex cases

### 4️⃣ Data Validation

Checks for missing mandatory fields.

### 5️⃣ Autonomous Decision Making

Agent:

* Evaluates completeness
* Avoids re-calling expensive APIs
* Applies routing logic

### 6️⃣ Routing Engine

Determines:

* Fast Track
* Manual Review
* Investigation
* Specialist Queue

### 7️⃣ Response Generation

Returns:

```json
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}
```

---

## 🧠 Key Features

* ✅ Hybrid AI extraction (Regex + LLM)
* ✅ Hallucination control
* ✅ Empty document detection
* ✅ Autonomous decision loop
* ✅ Explainable AI reasoning
* ✅ Full-stack implementation (React + FastAPI)
* ✅ Rate-limit handling & caching

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* pdfplumber
* Google Gemini

### Frontend

* React
* Axios

---

## 🚀 Setup Instructions

---

### 🔧 1. Clone Repository

```bash
git clone <your-repo-url>
cd insurance-claims-agent
```

---

### 🧠 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

#### ▶️ Run Backend

```bash
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 🔐 3. (Optional) Gemini API Setup

```bash
export GOOGLE_API_KEY="your_api_key"
```

> Note: Free tier has strict rate limits.

---

### 🎨 4. Frontend Setup

```bash
cd frontend
npm install
npm start
```

Open:

```
http://localhost:3000
```

---

## 📤 Usage

1. Open frontend UI
2. Upload FNOL document (PDF/TXT)
3. View:

   * Extracted fields
   * Missing fields
   * Recommended route
   * Reasoning
   * Raw JSON output

---

## ⚠️ Known Limitations

* Blank FNOL templates return null values (by design)
* LLM usage limited by API quota
* PDF extraction depends on document quality

---

## 🔥 Future Improvements

* Confidence scoring
* Batch processing
* Drag & drop UI
* Deployment (Render + Vercel)
* Vector DB (RAG) for claim history
* Fraud detection ML model

---

## 🧠 How This Stands Out

This is not just parsing — it is:

> ✅ An autonomous AI agent with decision-making
> ✅ Hybrid extraction pipeline
> ✅ Explainable routing logic
> ✅ Production-ready architecture

---

## 👨‍💻 Author

Built as a real-world AI + backend engineering project to demonstrate:

* Data extraction systems
* LLM integration
* System design thinking

---

## 📄 License

MIT License
