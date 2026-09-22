FAILURE_RULES = {
    "HTTP_500": "Server-side request failed",
    "HTTP_404": "Requested resource was not found",
    "TIMEOUT": "Server response timed out",
    "RETRY": "Application retried the failed request",
    "STATE_MISMATCH": "Application state became inconsistent",
    "CHECKOUT_STUCK": "Checkout flow did not complete"
}


def get_failure_description(event):
    return FAILURE_RULES.get(event, "Unknown event")