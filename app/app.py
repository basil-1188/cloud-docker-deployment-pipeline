from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Basil MK | Docker on EC2</title></head>
    <body style="font-family:sans-serif;background:#03060f;color:#e2e8f0;text-align:center;padding:80px;">
        <h1 style="color:#00c8ff">Docker App Running on AWS EC2</h1>
        <p>Deployed automatically via GitHub Actions CI/CD pipeline</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
