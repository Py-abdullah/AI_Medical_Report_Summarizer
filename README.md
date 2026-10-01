# 🩺 AI Medical Report Summarizer

An AI-powered application that simplifies complex medical reports into easy-to-understand, patient-friendly explanations.

## 📌 Overview

The AI Medical Report Summarizer allows users to upload medical reports in PDF or TXT format and generate a simplified summary using a language model.

The application is designed for educational and informational purposes. It does not provide medical diagnosis or replace professional medical advice.

## ✨ Features

- Upload medical reports in PDF or TXT format
- Extract text from PDF reports
- Generate AI-powered summaries
- Patient-friendly explanations
- Support for English, Urdu, and Arabic
- Highlights important findings
- Explains medical terminology
- Generates questions to discuss with a doctor
- Simple Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct
- PyPDF

## 📂 Project Structure

```text
AI_Medical_Report_Summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_data/
│   └── sample_medical_report.pdf
│
└── venv/
