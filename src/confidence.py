import re

def confidence_score(ocr_conf, value, field_type):
    if not value:
        return 0.3  # low confidence

    score = ocr_conf / 100

    # Pattern validation
    if field_type == "date":
        if re.match(r'\d{2}[/-]\d{2}[/-]\d{2,4}', str(value)):
            score += 0.2

    if field_type == "total":
        try:
            float(value)
            score += 0.2
        except:
            pass

    return min(score, 1.0)