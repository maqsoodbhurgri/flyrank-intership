from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Mini Backend API is running successfully",
        "status": "success"
    })

@app.route("/about")
def about():
    return jsonify({
        "name": "Maqsood Ahmed",
        "role": "Backend Learner",
        "project": "Mini Backend API",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
