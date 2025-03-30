from flask import Flask, request, jsonify

app = Flask(__name__)

# Maps subscriber IDs to their individual message queues
subscribers = {}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    subscriber_id = data.get('subscriber_id')
    if not subscriber_id:
        return jsonify({'error': 'subscriber_id is required'}), 400
    subscribers[subscriber_id] = []
    return jsonify({'status': f'{subscriber_id} subscribed'}), 200

@app.route('/publish', methods=['POST'])
def publish():
    data = request.get_json()
    message = data.get('message')
    target_id = data.get('subscriber_id')  # optional
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    if target_id:
        # Publish to a specific subscriber
        if target_id in subscribers:
            subscribers[target_id].append(message)
        else:
            return jsonify({'error': 'Subscriber not found'}), 400
    else:
        # Broadcast to all subscribers
        for sub_id in subscribers:
            subscribers[sub_id].append(message)

    return jsonify({'status': 'Message published'}), 200

@app.route('/retrieve', methods=['GET'])
def retrieve():
    subscriber_id = request.args.get('subscriber_id')
    if not subscriber_id or subscriber_id not in subscribers:
        return jsonify({'error': 'Subscriber not found'}), 400
    # Return and clear the subscriber's queue
    msgs = subscribers[subscriber_id]
    subscribers[subscriber_id] = []
    return jsonify({'messages': msgs}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)