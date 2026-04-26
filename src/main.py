import os
import json
from preprocess import preprocess
from ocr import extract_text
from extract import extract_fields
from confidence import confidence_score
from summary import generate_summary

# 🔥 Create folders first
os.makedirs("output/json", exist_ok=True)
os.makedirs("output/summary", exist_ok=True)

results = []

for file in os.listdir("data/raw"):
    try:
        path = f"data/raw/{file}"

        # Skip non-image files
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image = preprocess(path)
        text, conf = extract_text(image)

        # Skip low text cases
        if not text or len(text.strip()) < 10:
            print(f"⚠️ Low text detected in {file}")
            continue

        fields = extract_fields(text)

        # 🔥 FIXED: added field_type
        store_conf = confidence_score(conf, fields.get("store_name"), "store")
        date_conf = confidence_score(conf, fields.get("date"), "date")
        total_conf = confidence_score(conf, fields.get("total_amount"), "total")

        result = {
            "store_name": {
                "value": fields.get("store_name"),
                "confidence": store_conf,
                "low_confidence": store_conf < 0.7
            },
            "date": {
                "value": fields.get("date"),
                "confidence": date_conf,
                "low_confidence": date_conf < 0.7
            },
            "total_amount": {
                "value": fields.get("total_amount"),
                "confidence": total_conf,
                "low_confidence": total_conf < 0.7
            }
        }

        results.append(result)

        # 🔥 Fix filename (.jpg removed)
        filename = os.path.splitext(file)[0]

        with open(f"output/json/{filename}.json", "w") as f:
            json.dump(result, f, indent=2)

        print(f"✅ Processed {file}")

    except Exception as e:
        print(f"❌ Error processing {file}: {e}")

# 🔥 Generate summary correctly
summary = generate_summary(results)

with open("output/summary/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("🚀 Pipeline Completed Successfully")