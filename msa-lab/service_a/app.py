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
    
    # Call Service B
    response_b = requests.post('http://localhost:5001/service_b', json={"value": value})
    if response_b.status_code != 200:
        return jsonify({"error": "Service B failed"}), 500
    processed_value_b = response_b.json()['processed_value']
    
    # Call Service C
    response_c = requests.post('http://localhost:5002/service_c', json={"value": value})
    if response_c.status_code != 200:
        return jsonify({"error": "Service C failed"}), 500
    processed_value_c = response_c.json()['processed_value']

    return jsonify({"processed_value_b": processed_value_b, "processed_value_c": processed_value_c})

if __name__ == '__main__':
    app.run(port=5000)
