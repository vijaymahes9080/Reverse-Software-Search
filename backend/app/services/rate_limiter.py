import time
from typing import Dict, Tuple

class SimpleRateLimiter:
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: Dict[str, list] = {}

    def is_allowed(self, client_ip: str) -> bool:
        now = time.time()
        client_history = self.requests.get(client_ip, [])
        # Filter out requests outside the time window
        client_history = [t for t in client_history if now - t < self.window_seconds]
        
        if len(client_history) < self.max_requests:
            client_history.append(now)
            self.requests[client_ip] = client_history
            return True
        return False

rate_limiter = SimpleRateLimiter()
