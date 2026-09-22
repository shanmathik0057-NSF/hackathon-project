def analyze_events(events):
    print("BugLens Analysis Started")
    print("=" * 30)

    print("\nEvents received:")

    for event in events:
        print("-", event)


events = [
    "PAY_CLICK",
    "PAYMENT_REQUEST",
    "HTTP_500",
    "RETRY",
    "STATE_MISMATCH",
    "CHECKOUT_STUCK"
]

analyze_events(events)