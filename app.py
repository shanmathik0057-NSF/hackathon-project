from flask import Flask, request, jsonify

from analyzer import analyze_events

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "BugLens Backend is running"
    })


@app.route("/events", methods=["POST"])
def receive_events():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON data received"
        }), 400

    events = data.get("events")

    if not events:
        return jsonify({
            "error": "events field is required"
        }), 400

    result = analyze_events(events)

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)