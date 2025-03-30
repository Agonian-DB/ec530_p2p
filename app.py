from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for messages (not suitable for production)
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Message content is required'}), 400
    messages.append(data['message'])
    return jsonify({'status': 'Message received'}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)