def detect_root_cause(events):

    if (
        "HTTP_500" in events
        and "RETRY" in events
        and "STATE_MISMATCH" in events
    ):
        return {
            "cause": "Server failure caused retry followed by application state inconsistency.",
            "severity": "HIGH",
            "confidence": 0.92
        }

    if "HTTP_500" in events:
        return {
            "cause": "Server-side request failure detected.",
            "severity": "HIGH",
            "confidence": 0.75
        }

    if "TIMEOUT" in events:
        return {
            "cause": "Request exceeded the expected response time.",
            "severity": "MEDIUM",
            "confidence": 0.80
        }

    return {
        "cause": "No clear root cause detected.",
        "severity": "LOW",
        "confidence": 0.40
    }