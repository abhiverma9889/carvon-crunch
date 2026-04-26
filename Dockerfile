FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# 🔥 FIX: install required system libs
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]