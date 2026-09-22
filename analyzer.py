from event_parser import load_events, extract_event_names
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


event_data = load_events("events.json")

events = extract_event_names(event_data)

analyze_events(events)