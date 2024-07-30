from ast import Import
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)

file_path = "C:/Users/TERREL BRAGANCA/chatbot/Script_thingamajig/session.csv"

@app.route('/log_click', methods=['POST'])
def log_click():
    data = request.json  # Get the JSON data from the request
    if not data or 'timestamp' not in data or 'element' not in data:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

    with open(file_path,mode='a',newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([data.get('textContent')])

    processed_data = {
        'status': 'success',
        'message': f"Received click on {data.get('element', 'unknown element')}",
        'received_at': data['timestamp']
    }
    
    print(processed_data)

    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)

