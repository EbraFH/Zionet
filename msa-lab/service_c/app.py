# service_c/app.py
from flask import Flask, request, jsonify
import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
ptvsd.wait_for_attach()

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
