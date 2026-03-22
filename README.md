# Full_Stack_assignment

# Mini Clinical Data Reconciliation Engine

A full-stack AI-powered platform designed to reconcile conflicting patient medication records and audit data quality for clinical safety.

## 🚀 Quick Start

### Backend (Python)
1. Navigate to `/backend`
2. Create a `.env` file and add: `OPENAI_API_KEY=your_key_here`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn main:app --reload`

### Frontend (React)
1. Navigate to `/frontend`
2. Install dependencies: `npm install`
3. Run the app: `npm run dev`

---

## 🧠 AI Integration & Prompt Strategy
I utilized **GPT-4o** for this project due to its high clinical reasoning accuracy and reliable JSON output mode.

### Prompt Engineering Approach:
* **Chain of Thought:** The model is instructed to first evaluate "Recency" (timestamps) vs "Reliability" (Source type) before determining the truth.
* **Clinical Guardrails:** Explicit instructions were added to the `Data Quality` prompt to flag physiological impossibilities (e.g., Blood Pressure > 250) as "High Severity" issues.
* **Output Consistency:** Used OpenAI's JSON Mode to ensure the frontend can reliably parse reasoning and confidence scores without text artifacts.

---

## 🛠 Architecture Decisions
- **FastAPI:** Chosen for its high performance and automatic Pydantic validation, which is critical for handling sensitive medical data structures.
- **Modular Services:** Reconciliation and Validation logic are separated into a `/services` layer to keep `main.py` clean and allow for independent unit testing.
- **Stateless Design:** The API is stateless to mimic a real-world microservice that could be easily containerized or scaled.

---

## 🧪 Testing
Run tests using: `pytest`
- **Core Logic Tests:** Covers medication conflict resolution logic.
- **Boundary Tests:** Ensures vital signs outside human limits are flagged correctly.
- **Schema Tests:** Validates that API inputs conform to expected clinical formats.

---

## 📈 Future Improvements
1. **Caching:** Implement Redis to cache reconciliation results for identical patient profiles to reduce API costs.
2. **HL7/FHIR Integration:** Adapt the input schemas to follow international healthcare data standards.
3. **Human-in-the-loop:** Add a "Verified by Clinician" flag to the database to improve the AI's confidence calibration over time.

**Estimated Time Spent:** X Hours
