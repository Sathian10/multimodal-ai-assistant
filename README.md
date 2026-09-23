# Multimodal AI Assistant

## Final Year Project

**Project Title:** Design and Evaluation of a Multimodal AI Assistant Using Cascaded Pre-trained AI Models

This project implements a multimodal AI assistant that integrates multiple pre-trained AI models within a single Streamlit web application. The system demonstrates AI model orchestration by processing different input modalities and producing sentiment analysis results.

## Supported Input Pathways

The application supports five processing pathways:

1. **Uploaded Audio**  
   Audio → Whisper Speech Recognition → Text → DistilBERT Sentiment Analysis

2. **Live Microphone Recording**  
   Microphone → Whisper Speech Recognition → Text → DistilBERT Sentiment Analysis

3. **Live Typed Text**  
   Typed Text → DistilBERT Sentiment Analysis

4. **Uploaded Text File**  
   TXT File → DistilBERT Sentiment Analysis

5. **Uploaded Image**  
   Image → Tesseract OCR → Extracted Text → DistilBERT Sentiment Analysis

## Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- DistilBERT
- Hugging Face Transformers
- PyTorch
- Tesseract OCR
- streamlit-keyup

## Installation

Install the Python dependencies:

```bash
pip install -r requirements.txt
