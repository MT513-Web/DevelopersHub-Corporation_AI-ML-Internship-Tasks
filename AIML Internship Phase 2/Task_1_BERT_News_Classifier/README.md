
# Task 1: BERT-Based News Classification System

## Project Overview
This project implements a professional-grade news classification dashboard using the **BERT (Bidirectional Encoder Representations from Transformers)** architecture. The model has been fine-tuned on the AG News dataset to categorize headlines into four distinct sectors with high precision.

## Performance Metrics
- **Validation Accuracy:** 94.5%
- **Frameworks:** PyTorch, Hugging Face Transformers
- **Interface:** Streamlit Dashboard

## Features
- **Deep Learning Backend:** Powered by Hugging Face Transformers and PyTorch.
- **Real-time Inference:** Classifies news headlines into World, Sports, Business, or Sci/Tech categories.
- **Confidence Scoring:** Provides a probability distribution and confidence percentage for every prediction.
- **Interactive UI:** Built with Streamlit for a seamless user experience.

## Project Structure
- `app.py`: The main application script featuring the Streamlit UI and inference logic.
- `requirements.txt`: Configuration file listing all necessary Python dependencies.
- `README.md`: Documentation and setup guide.

## Setup & Installation

### 1. Download the Model
Due to GitHub's file size restrictions, the trained model weights (~420MB) are hosted on Google Drive.
- **Download Link:** https://drive.google.com/open?id=1s_jaTa_7LvUbkE-EASBdh4lTjSakDiLy&usp=drive_fs
- **Instruction:** Download and extract the folder named `news_classifier_bert_v1` into this directory.

### 2. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install -r requirements.txt