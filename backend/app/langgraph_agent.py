import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0
)


def ask_ai(user_message: str):
    prompt = f"""
You are an AI CRM assistant.

Extract the interaction details from the user message.

Return ONLY valid JSON.

Format:

{{
    "hcp_name":"",
    "interaction_type":"",
    "date":"",
    "time":"",
    "attendees":"",
    "topics":"",
    "materials":"",
    "samples":"",
    "sentiment":"",
    "outcomes":"",
    "followup":""
}}

User:
{user_message}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown if present
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    return json.loads(content)