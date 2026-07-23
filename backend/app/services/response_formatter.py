from typing import Any, Dict, Optional

def success_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """
    Returns a standardized API success payload.
    """
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(detail: str, code: int = 400) -> Dict[str, Any]:
    """
    Returns a standardized API error payload.
    """
    return {
        "status": "error",
        "code": code,
        "detail": detail
    }
