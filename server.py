from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/log_click', methods=['POST'])
def log_click():
    data = request.json  # Get the JSON data from the request
    if not data or 'timestamp' not in data or 'element' not in data:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

    print('Received data:', data)

    processed_data = {
        'status': 'success',
        'message': f"Received click on {data.get('element', 'unknown element')}",
        'received_at': data['timestamp']
    }

    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
