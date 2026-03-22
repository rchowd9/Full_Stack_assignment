from utils.llm_client import llm_client

SYSTEM_PROMPT = """
You are a Clinical Data Auditor. Evaluate the quality of a patient record.
Check for:
1. Completeness (Missing fields or empty arrays).
2. Accuracy (Physiological impossibilities like BP 340/180 or Heart Rate 0).
3. Timeliness (Data older than 6 months).

Return a JSON object:
{
  "overall_score": int (0-100),
  "breakdown": { "completeness": int, "accuracy": int, "timeliness": int, "clinical_plausibility": int },
  "issues_detected": [ { "field": str, "issue": str, "severity": "low"|"medium"|"high" } ]
}
"""

async def run_validation(data: dict):
    user_content = f"Audit this record: {data}"
    return await llm_client.get_json_completion(SYSTEM_PROMPT, user_content)
