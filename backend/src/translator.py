"""Natural language to SQL translator.

This module provides a translator that converts natural language questions
into SQL queries using OpenAI's GPT-4o model.
"""

import json
import logging
from typing import Dict, Any

import openai
from tenacity import retry, stop_after_attempt, wait_exponential

from .settings import settings

# Configure OpenAI client
client = openai.AsyncOpenAI(api_key=settings.openai_api_key)

# System prompt for the LLM
SYSTEM_PROMPT = """You are a secure SQL generator that converts natural language questions into SQL queries.
Your task is to generate ONLY SELECT statements that are safe and efficient.

Rules:
1. ONLY generate SELECT statements - never UPDATE, DELETE, INSERT, DROP, etc.
2. Use proper SQL syntax and best practices
3. Return ONLY the SQL query without any explanation
4. If the question cannot be translated to a SELECT statement, return "-- BLOCKED"
5. If you're unsure about the translation, return "-- TODO"

Format your response as a JSON object with a single "sql" field containing the SQL query.
Example: {"sql": "SELECT * FROM customers WHERE name LIKE '%John%'"}
"""

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    reraise=True
)
async def translate(question: str) -> str:
    """Translate a natural language question into SQL using OpenAI's GPT-4o.
    
    Args:
        question: The natural language question to translate
        
    Returns:
        str: The corresponding SQL query, "-- TODO" if translation not available,
             or "-- BLOCKED" if the query is not a SELECT statement
    """
    try:
        # Call OpenAI API
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            response_format={"type": "json_object"},
            timeout=10.0  # 10 second timeout
        )
        
        # Parse the response
        content = response.choices[0].message.content
        result = json.loads(content)
        
        # Return the SQL query
        return result.get("sql", "-- TODO")
    
    except Exception as e:
        logging.error(f"Error translating question: {str(e)}")
        return "-- TODO" 