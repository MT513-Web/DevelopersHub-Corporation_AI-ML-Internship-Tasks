import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F
import pandas as pd

# Path to the local model directory
MODEL_PATH = "./news_classifier_bert_v1"

@st.cache_resource
def load_model_assets():
    """Load the fine-tuned BERT model and tokenizer from local disk."""
    tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
    model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
    return tokenizer, model

# Initialize model and labels
tokenizer, model = load_model_assets()
label_names = ["World", "Sports", "Business", "Sci/Tech"]

# --- Streamlit UI Configuration ---
st.set_page_config(page_title="News Analytics Dashboard", layout="wide")

# Sidebar for Technical Specifications
with st.sidebar:
    st.title("Project Information")
    st.markdown("""
    **Core Architecture:**
    * Model: BERT Base Uncased
    * Task: Multi-class Classification
    * Framework: PyTorch & Transformers
    """)
    st.write("---")
    st.subheader("Classification Labels")
    for label in label_names:
        st.write(f"* {label}")

# Main Interface Header
st.title("News Category Analysis Tool")
st.write("Analyze news headlines using a fine-tuned BERT model for precise categorization.")

# User Input Section
user_input = st.text_area("Input News Headline:", height=120, placeholder="Paste news content here for analysis...")

# Layout Columns for Results
col1, col2 = st.columns([1, 1])

if st.button("Analyze Content"):
    if user_input.strip():
        # Tokenization
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=128)
        
        # Model Inference
        with torch.no_grad():
            outputs = model(**inputs)
            # Calculate Probabilities for Confidence Scoring
            probabilities = F.softmax(outputs.logits, dim=-1)
            prediction_idx = torch.argmax(probabilities, dim=-1).item()
            confidence_score = probabilities[0][prediction_idx].item() * 100

        # Display Category and Confidence
        with col1:
            st.subheader("Analysis Summary")
            st.info(f"**Predicted Category:** {label_names[prediction_idx]}")
            st.write(f"**Confidence Level:** {confidence_score:.2f}%")
            
            # Progress bar for visual representation of confidence
            st.progress(confidence_score / 100)

        # Display Probability Distribution Chart
        with col2:
            st.subheader("Probability Distribution")
            chart_df = pd.DataFrame({
                'Category': label_names,
                'Score': probabilities[0].tolist()
            })
            st.bar_chart(chart_df.set_index('Category'))
            
    else:
        st.error("Input required: Please enter text to proceed with classification.")

st.write("---")
st.caption("Technical Internship Phase 2: Text Classification System")