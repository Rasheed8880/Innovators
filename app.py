from flask import Flask, render_template, request, jsonify
import pickle
import os
import uuid

from utils.fetch_link_content import fetch_link_text
from utils.ocr_image import extract_text_from_image


from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend JS calls

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model
model_path = os.path.join('model', 'model.pkl')
with open(model_path, 'rb') as f:
    model, vectorizer = pickle.load(f)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Result after checking input
@app.route('/check', methods=['POST'])
def check():
    input_type = request.form['input_type']
    text = ""

    if input_type == 'text':
        text = request.form.get('input', '').strip()

    elif input_type == 'link':
        url = request.form.get('input', '')
        text = fetch_link_text(url)

    elif input_type == 'image':
        image_file = request.files.get('input')
        if image_file and image_file.filename != "":
            filename = str(uuid.uuid4()) + "_" + image_file.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            text = extract_text_from_image(image_path)
            os.remove(image_path)  # Clean up

    # Handle empty content
    if not text.strip():
        result = "Unable to extract any content."
        stars = 0
        reference_links = []
    else:
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        probas = model.predict_proba(X)[0]
        confidence = max(probas)
        stars = round(confidence * 5)

        result = "✅ Likely Real Information" if prediction == 1 else "❌ Likely Fake Information"
        reference_links = get_references(text)

    return render_template('result.html', result=result, stars=stars, reference_links=reference_links)



# Dummy reference function
def get_references(text):
    return [
        "https://www.who.int",
        "https://www.ncbi.nlm.nih.gov",
        "https://www.cdc.gov"
    ]

if __name__ == '__main__':
    app.run(debug=True)
