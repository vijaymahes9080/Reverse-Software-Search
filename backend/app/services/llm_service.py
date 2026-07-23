import json
import logging
from typing import Dict, Any, List
import litellm
from app.config import settings

logger = logging.getLogger(__name__)

def call_llm(prompt: str, response_format: str = "text") -> str:
    """
    Call the LLM (using LiteLLM) with a system prompt and a user prompt.
    Includes fallbacks for mock mode or api errors.
    """
    if settings.MOCK_LLM or not settings.OPENAI_API_KEY:
        logger.info("Mock LLM enabled or OpenAI key missing. Using simulated response.")
        raise ValueError("Mock LLM Mode")

    try:
        # Check if custom api base is configured
        extra_args = {}
        if settings.LITELLM_API_BASE:
            extra_args["api_base"] = settings.LITELLM_API_BASE
        
        response = litellm.completion(
            model=settings.LITELLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a professional CTO and Software Synthesis Engine. You output precise details, code snippets, architectural details, and diagrams based on user requirements. Always output clean, parsing-safe strings."},
                {"role": "user", "content": prompt}
            ],
            api_key=settings.OPENAI_API_KEY,
            **extra_args
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error calling LiteLLM: {str(e)}")
        raise e

def call_llm_json(prompt: str, schema_class=None) -> Dict[str, Any]:
    """
    Call the LLM and return a parsed JSON object.
    """
    system_prompt = (
        "You are an expert software architect AI. Return ONLY a valid JSON object matching the requested schema. "
        "Do not wrap your output in ```json ... ``` blocks or add any conversational text. "
        "Strictly return clean, parseable JSON."
    )
    
    if settings.MOCK_LLM or not settings.OPENAI_API_KEY:
        raise ValueError("Mock LLM Mode")

    try:
        extra_args = {}
        if settings.LITELLM_API_BASE:
            extra_args["api_base"] = settings.LITELLM_API_BASE

        # We can request JSON format from LiteLLM
        response = litellm.completion(
            model=settings.LITELLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            api_key=settings.OPENAI_API_KEY,
            response_format={"type": "json_object"},
            **extra_args
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        logger.error(f"Error parsing JSON from LLM: {str(e)}")
        raise e
