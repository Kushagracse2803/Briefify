import os
from flask import Flask, render_template, request, jsonify
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from evaluate import load
import torch
import nltk
from nltk import tokenize
import fitz  # PyMuPDF for PDF text extraction
import pytesseract
from PIL import Image
import logging

# Download required NLTK data
nltk.download('punkt')

app = Flask(__name__)

# Limit upload size to 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Ensure logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

# Model name or path
MODEL_NAME = "google/pegasus-xsum"

# Set device to GPU if available else CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load tokenizer and model
tokenizer = PegasusTokenizer.from_pretrained(MODEL_NAME)
model = PegasusForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

# Load ROUGE metric (optional)
rouge_metric = load("rouge")

@app.route('/')
def index():
    # Render home page
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json(force=True)
        text = data.get('text', '').strip()
        length = data.get('length', 'medium').lower()

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Set max length based on summary length parameter
        if length == 'short':
            max_len = 80
        elif length == 'long':
            max_len = 220
        else:
            max_len = 140

        # Tokenize input text
        inputs = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)

        # Generate summary
        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_len,
            min_length=int(max_len * 0.6),
            num_beams=8,
            length_penalty=1.5,
            early_stopping=True
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

        return jsonify({'summary': summary})

    except Exception as e:
        logging.error(f"Summarize error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        if file.filename.lower().endswith('.pdf'):
            # Extract text from PDF using PyMuPDF
            doc = fitz.open(stream=file.read(), filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
        elif file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Extract text from image using pytesseract OCR
            image = Image.open(file.stream)
            text = pytesseract.image_to_string(image)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        return jsonify({'extracted_text': text})

    except Exception as e:
        logging.error(f"Upload error: {e}")
        return jsonify({'error': f"Failed to extract text: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
