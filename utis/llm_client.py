import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o"  # High reasoning capability for clinical data

    async def get_json_completion(self, system_prompt: str, user_content: str):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            # In a real app, log this to a service like Sentry
            print(f"LLM Error: {e}")
            return {"error": "Failed to process clinical data", "details": str(e)}

llm_client = LLMClient()
