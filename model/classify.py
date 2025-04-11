def classify_input(text):
    if "cure" in text.lower():
        return {
            "verdict": "Possibly Fake",
            "rating": 2,
            "message": "Be cautious, always verify medical claims with professionals.",
            "references": ["https://www.who.int", "https://www.cdc.gov"]
        }
    else:
        return {
            "verdict": "Likely Real",
            "rating": 4,
            "message": "The information appears reliable.",
            "references": ["https://www.nih.gov"]
        }
