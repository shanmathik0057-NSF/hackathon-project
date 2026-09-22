from flask import Flask, request, jsonify

app = Flask(__name__)

events = []


@app.route("/")
def home():
    return jsonify({
        "message": "BugLens Backend is running"
    })


@app.route("/events", methods=["POST"])
def receive_event():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No event data received"
        }), 400

    events.append(data)

    return jsonify({
        "message": "Event received successfully",
        "event": data
    }), 201


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


if __name__ == "__main__":
    app.run(debug=True)
    