# EC530 P2P Chat System and Message API

This project includes a simple P2P (peer-to-peer) chat system using sockets, a RESTful API for message management, and a basic publish-subscribe model using Flask.

## Files Overview

### 1. `server.py`
- Basic TCP server that listens for client connections and echoes received messages.

### 2. `client.py`
- Basic TCP client that sends user input to the server and displays responses.

### 3. `client_async.py`
- Asynchronous client that simultaneously listens for messages while sending user input.

### 4. `app.py`
- Flask-based API for sending and retrieving messages.
- Endpoints:
  - `POST /send` – Send a message.
  - `GET /messages` – Retrieve all messages.

### 5. `pubsub.py`
- Basic publish-subscribe system using Flask.
- Endpoints:
  - `POST /subscribe` – Register a subscriber.
  - `POST /publish` – Publish a message.
  - `GET /retrieve?subscriber_id=<ID>` – Retrieve messages for a specific subscriber.

---

## How to Run

### Run the TCP Server
```bash
python server.py
