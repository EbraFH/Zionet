# service_a/app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/service_a', methods=['POST'])
def service_a():
    data = request.json
    if 'value' not in data:
        return jsonify({"error": "Invalid data"}), 400

    value = data['value']
    response = requests.post('http://localhost:5001/service_b', json={"value": value})

    if response.status_code != 200:
        return jsonify({"error": "Service B failed"}), 500

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)
