from flask import Flask, request, jsonify
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API
API_KEY = "AIzaSyAzYCvkTv0xKo7WjnGmQ5o-n_aP7ZwrzIg"
genai.configure(api_key=API_KEY)

# Create a Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return "🤖 Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Get response from Gemini
        response = model.generate_content(user_message)

        return jsonify({
            "user_message": user_message,
            "bot_reply": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
