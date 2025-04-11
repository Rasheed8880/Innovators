from flask import Flask, render_template, request
import pickle
from utils.fetch_link_content import fetch_link_text
from utils.ocr_image import extract_text_from_image
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join('model', r'model.pkl')
with open(model_path, 'rb') as f:    
    model, vectorizer = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    input_type = request.form['input_type']
    user_input = request.form['input']

    # Extract meaningful text based on input type
    if input_type == 'text':
        text = user_input
    elif input_type == 'link':
        text = fetch_link_text(user_input)
    elif input_type == 'image':
        text = extract_text_from_image(user_input)
    else:
        text = ""

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

        if prediction == 1:
            result = "Likely Real Information"
        else:
            result = "Likely Fake Information"

        reference_links = get_references(text)

    return render_template('result.html', result=result, stars=stars, reference_links=reference_links)

def get_references(text):
    # You can replace this with a proper search API or a static list for now
    references = [
        "https://www.who.int",
        "https://www.ncbi.nlm.nih.gov",
        "https://www.cdc.gov",
    ]
    return references

if __name__ == '__main__':
    app.run(debug=True)