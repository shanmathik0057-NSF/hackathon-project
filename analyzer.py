from rules import get_failure_description
from explanation import generate_explanation


def analyze_events(events):

    print("======================================")
    print("          BUGLENS ANALYZER")
    print("======================================")

    print("\nEVENT TIMELINE")
    print("--------------------------------------")

    for index, event in enumerate(events, start=1):
        print(f"{index}. {event}")

    print("\nFAILURES DETECTED")
    print("--------------------------------------")

    for event in events:

        description = get_failure_description(event)

        if description != "Unknown event":
            print(f"⚠ {event}: {description}")

    print("\nBUG EXPLANATION")
    print("--------------------------------------")

    explanations = generate_explanation(events)

    for explanation in explanations:
        print("→", explanation)


events = [
    "PAY_CLICK",
    "PAYMENT_REQUEST",
    "HTTP_500",
    "RETRY",
    "STATE_MISMATCH",
    "CHECKOUT_STUCK"
]

analyze_events(events)