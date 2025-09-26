from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    return jsonify({"events": ["Hackathon", "Cultural Fest"]})

if __name__ == "__main__":
    app.run(port=6000)
