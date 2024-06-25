# service_b/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/service_b', methods=['POST'])
def service_b():
    data = request.json
    value = data.get('value')
    if value is None:
        return jsonify({"error": "Invalid data"}), 400

    # Simulate data processing (e.g., read from a database)
    processed_value = value * 2

    return jsonify({"processed_value": processed_value})

if __name__ == '__main__':
    app.run(port=5001)
