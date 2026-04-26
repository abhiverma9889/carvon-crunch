import re

def extract_fields(text):
    lines = text.split("\n")

    # Store name = first meaningful line
    store = next((l for l in lines if len(l.strip()) > 3), None)

    # Date patterns
    date_match = re.search(r'\d{2}[/-]\d{2}[/-]\d{2,4}', text)

    # Total detection
    total_match = re.search(r'(total|amount|grand total)[^\d]*(\d+\.\d{2})', text.lower())

    total = total_match.group(2) if total_match else None

    return {
        "store_name": store,
        "date": date_match.group() if date_match else None,
        "total_amount": total
    }