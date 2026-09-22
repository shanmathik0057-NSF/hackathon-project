import json


def load_events(filename):

    with open(filename, "r") as file:
        data = json.load(file)

    return data


def extract_event_names(event_data):

    return [
        item["event"]
        for item in event_data
    ]