from typing import Tuple

def validate_prompt(prompt: str) -> Tuple[bool, str]:
    """
    Validates natural language prompt input.
    """
    if not prompt or not isinstance(prompt, str):
        return False, "Prompt must be a non-empty string."
    
    clean_prompt = prompt.strip()
    if len(clean_prompt) < 3:
        return False, "Prompt is too short. Please enter at least 3 characters."
        
    if len(clean_prompt) > 1000:
        return False, "Prompt exceeds maximum length of 1000 characters."
        
    return True, "Valid prompt."
