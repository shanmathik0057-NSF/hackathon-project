def generate_explanation(events):

    explanation = []

    if "PAY_CLICK" in events:
        explanation.append(
            "User initiated the payment flow."
        )

    if "PAYMENT_REQUEST" in events:
        explanation.append(
            "Application sent a payment request."
        )

    if "HTTP_500" in events:
        explanation.append(
            "Payment server returned HTTP 500."
        )

    if "RETRY" in events:
        explanation.append(
            "Application retried the failed request."
        )

    if "STATE_MISMATCH" in events:
        explanation.append(
            "Application entered an inconsistent state."
        )

    if "CHECKOUT_STUCK" in events:
        explanation.append(
            "Checkout flow failed to complete."
        )

    return explanation