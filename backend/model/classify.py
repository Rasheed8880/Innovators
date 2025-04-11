from transformers import pipeline

classifier = pipeline("text-classification", model="davanstrien/bertweet-misinformation", tokenizer="vinai/bertweet-base")

def classify_input(text):
    output = classifier(text)[0]
    label = output["label"]
    score = output["score"]

    if label == "true":
        verdict = "✅ This appears to be accurate information."
        rating = 5
    else:
        verdict = "❌ This appears to be false medical information!"
        rating = 1

    return {
        "verdict": verdict,
        "rating": rating,
        "message": f"Confidence: {round(score * 100, 2)}%",
        "references": [
            "https://www.who.int/",
            "https://www.cdc.gov/",
            "https://medlineplus.gov/"
        ] if label != "true" else []
    }
