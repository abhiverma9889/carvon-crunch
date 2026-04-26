# 🧾 Receipt OCR & Expense Analysis System

## 📌 Objective
Build a system to extract structured information from semi-structured receipt images and generate reliable, confidence-aware outputs for downstream applications.

---

## 🧠 Approach

The pipeline follows this flow:

### 1. Image Preprocessing
- Converted images to grayscale
- Applied Gaussian blur for noise reduction
- Thresholding for better OCR accuracy

### 2. OCR (Text Extraction)
- Used **Tesseract OCR**
- Extracted text along with confidence score

### 3. Key Information Extraction
Extracted fields using regex and heuristics:
- Store Name (top line)
- Date (pattern matching)
- Total Amount (keywords like "Total")

### 4. Data Structuring
Each receipt is converted into structured JSON:

```json
{
  "store_name": {
    "value": "Reliance Mart",
    "confidence": 0.92
  },
  "date": {
    "value": "12/03/2024",
    "confidence": 0.88
  },
  "total_amount": {
    "value": "456.50",
    "confidence": 0.95
  }
}
