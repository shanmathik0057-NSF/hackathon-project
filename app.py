from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "BugLens Backend is running"
    })

@app.route("/events", methods=["POST"])
def receive_event():
    data = request.get_json()

    print("Received event:", data)

    return jsonify({
        "status": "success",
        "message": "Event received",
        "event": data
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
