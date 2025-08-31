# 📖 Briefify – Free Text Summarizer  

> **Your personal AI-powered assistant for lightning-fast summaries.**  

![License](https://img.shields.io/badge/License-MIT-blue.svg)  
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)  
![Flask](https://img.shields.io/badge/Backend-Flask-orange.svg)  
![Transformers](https://img.shields.io/badge/NLP-Transformers-red.svg)  

**Briefify** is a modern, web-based summarization tool that transforms long documents, articles, or even images into **clear and concise summaries** in seconds. Powered by advanced AI models like **Pegasus**, it’s built to help **students, researchers, and professionals** save time and focus on what matters most.  

---

## 🚀 Features  

✅ **Smart Summarization** – Generate summaries in short, medium, or long formats.  
✅ **File Upload Support** – Upload **PDFs** or **images**; text is extracted automatically.  
✅ **OCR Integration** – Extract text from images using `pytesseract`.  
✅ **Responsive UI** – Simple, modern, and mobile-friendly interface.  
✅ **Customizable Output** – Choose summary length for different use cases.  
✅ **Lightweight & Fast** – Runs locally with minimal setup.  

---

## 🛠️ Tech Stack  

| Layer            | Tools Used                                                                 |
|------------------|---------------------------------------------------------------------------|
| **Frontend**     | HTML, CSS, JavaScript                                                     |
| **Backend**      | Python, Flask                                                             |
| **AI/NLP**       | 🤗 Transformers (Pegasus), PyTorch, NLTK, Evaluate                        |
| **File Handling**| PyMuPDF (PDFs), Pytesseract (OCR), Pillow                                 |

---

## 📦 Installation  

Clone this repo and set up your environment:  

bash
git clone https://github.com/yourusername/briefify.git
cd briefify

1️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate           # On Windows: venv\Scripts\activate
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the App
python app.py
Visit the app in your browser: http://localhost:5000

📜 Requirements
All core dependencies are listed in requirements.txt.
Key packages include:

nginx
Copy code
flask
transformers
torch
evaluate
nltk
pymupdf
pytesseract
Pillow
sentencepiece
absl-py
rouge-score

📂 Project Structure

briefify/
├── app.py               # Flask app entry point
├── templates/           # Frontend templates (HTML)
├── static/              # CSS, JS, Images
├── summarizer.py        # Core summarization logic
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
📸 Screenshots

🤝 Contributing
Contributions are welcome!

Fork this repo

Create a branch: git checkout -b feature-name

Commit changes: git commit -m "Added new feature"

Push and create a PR

📜 License
This project is licensed under the MIT License – see LICENSE for details.

🌟 Future Ideas
🔹 Summarization for YouTube videos (speech-to-text + summary)

🔹 Dark mode UI 🌙

🔹 Browser extension for instant webpage summarization

🔹 Export summaries in PDF/Docx

# Summary 

  # Screenshots

  ![alt text](<Screenshot 2025-08-31 222040.png>)
  ![alt text](<Screenshot 2025-08-31 222415.png>)
