import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def reconcile_medication(data: dict):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": RECONCILIATION_PROMPT},
                  {"role": "user", "content": str(data)}],
        response_format={ "type": "json_object" }
    )
    return response.choices[0].message.content
