from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_cors import CORS
from jsonschema import ValidationError
from chat import get_response, models 
import logging
app = Flask(__name__)
CORS(app)

@app.route("/welcome", methods=['GET'])
def welcome():
    welcome_messages = [
        "Welcome to the chatbot! How can I assist you today?",
        "You can ask me about the weather.",
        "Feel free to say 'hello' or ask me anything else!",
        "I'm here to help you with your queries."
    ]
    return jsonify({"messages": welcome_messages})

@app.route("/predict", methods=["POST"])
def predict():
    logging.info("Received request: %s", request.json)

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    text = data["message"]

    logging.info("Processing message: %s", text)

    if len(text) == 0:
        return jsonify({"error": "Message cannot be empty"}), 400

    if "urgent" in text.lower():
        logging.info("Received an urgent message: %s", text)

    try:
        response = get_response(text, models)
        print("Response:", response)
        print("ques", )
    except Exception as e:
        logging.error("Error in get_response: %s", str(e))
        return jsonify({"error": "An error occurred while processing your request."}), 500

    message = {"answer": response}

    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)