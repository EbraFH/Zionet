# service_c/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/service_c', methods=['POST'])
def service_c():
    data = request.json
    value = data.get('value')
    if value is None:
        return jsonify({"error": "Invalid data"}), 400

    # Simulate data processing
    processed_value = value + 10

    return jsonify({"processed_value": processed_value})

if __name__ == '__main__':
    app.run(port=5002)
