from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key for the Google Generative AI service
genai.configure(api_key="AIzaSyDpunef5zs8EeVQ3da45fnu5q21JCczI20")

# Define the generation configuration for the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

# Create the GenerativeModel instance with the specified configuration
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)


@app.route("/get_orphanages", methods=["POST"])
def get_orphanages():
    location = request.json.get("location")

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": ["orphanages near me\n"],
            },
            {
                "role": "model",
                "parts": [
                    "I need to know your location to find orphanages near you. \n\nPlease tell me: \n\n* *What city and state/province/country are you in?* \n\nOnce I have your location, I can help you find orphanages in your area. \n"
                ],
            },
            {
                "role": "user",
                "parts": [f"my location is {location}\n"],
            },
            {
                "role": "model",
                "parts": [
                    f"I need a bit more information to understand your location! '{location}' seems to be a common name.  \n\nTo help me find orphanages near you, please tell me:\n\n* *What city and state is {location} in?* For example, is it in Hyderabad, Telangana? \n\nOnce I know the full location, I can be more helpful. \n"
                ],
            },
        ]
    )

    response = chat_session.send_message(f"orphanages in {location}")

    return jsonify({"response": response.text})


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "_main_":
    app.run(debug=True)
