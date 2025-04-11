from flask import Flask, request, jsonify
from flask_cors import CORS
from model.classify import classify_input
from utils.fetch_link_content import get_text_from_url
from utils.ocr_image import extract_text_from_image

app = Flask(_name_)
CORS(app)

@app.route("/api/check", methods=["POST"])
def check():
    data = request.json
    input_type = data["input_type"]
    input_value = data["input"]

    if input_type == "text":
        text = input_value
    elif input_type == "link":
        text = get_text_from_url(input_value)
    elif input_type == "image":
        text = extract_text_from_image(input_value)
    else:
        return jsonify({"error": "Invalid input type"}), 400

    result = classify_input(text)
    return jsonify(result)

if _name_ == "_main_":
    app.run(debug=True)