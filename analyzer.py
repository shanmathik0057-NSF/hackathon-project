from rules import get_failure_description
from explanation import generate_explanation
from root_cause import detect_root_cause


def analyze_events(events):

    failures = []

    for event in events:

        description = get_failure_description(event)

        if description != "Unknown event":

            failures.append({
                "event": event,
                "description": description
            })

    explanations = generate_explanation(events)

    root_cause = detect_root_cause(events)

    result = {
        "events": events,
        "failures": failures,
        "explanation": explanations,
        "root_cause": root_cause
    }

    return result

if __name__ == "__main__":

    events = [
        "PAY_CLICK",
        "PAYMENT_REQUEST",
        "HTTP_500",
        "RETRY",
        "STATE_MISMATCH",
        "CHECKOUT_STUCK"
    ]

    result = analyze_events(events)

    print("\nBUGLENS ANALYSIS RESULT")
    print("=" * 40)

    print("\nFAILURES:")

    for failure in result["failures"]:
        print(
            failure["event"],
            "→",
            failure["description"]
        )

    print("\nEXPLANATION:")

    for explanation in result["explanation"]:
        print("→", explanation)

    print("\nROOT CAUSE:")
    print(result["root_cause"]["cause"])

    print(
        "Severity:",
        result["root_cause"]["severity"]
    )

    print(
        "Confidence:",
        result["root_cause"]["confidence"]
    )