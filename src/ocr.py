import pytesseract

def extract_text(image):
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    words = []
    confidences = []

    for i in range(len(data['text'])):
        word = data['text'][i].strip()
        conf = int(data['conf'][i])

        if word != "" and conf > 0:
            words.append(word)
            confidences.append(conf)

    full_text = " ".join(words)
    avg_conf = sum(confidences) / len(confidences) if confidences else 0

    return full_text, avg_conf