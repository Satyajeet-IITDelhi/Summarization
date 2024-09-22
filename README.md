Text Summarization API using Fine-tuned Language Model
Overview
This project involves fine-tuning a pre-trained language model (LLM) for text summarization and deploying a RESTful API to allow interaction with the model. Users can submit text via a POST request, and the model will return a concise summary of the input text.

Key Features:
Trained a BART (or chosen LLM) model for summarization.
Deployed a RESTful API using FastAPI to interact with the model.
Accepts text input and generates a summarized output.
Model Training Process
Dataset: Used a public summarization dataset from Hugging Face Datasets (e.g., CNN/DailyMail).
Pre-trained Model: Fine-tuned facebook/bart-large-cnn using Hugging Face's Transformers library.
Training Framework: Hugging Face's transformers library with PyTorch backend was used for fine-tuning.
Before and After Fine-tuning:
The pre-trained model was initially able to generate basic summaries.
After fine-tuning, the model became more accurate in summarizing longer and domain-specific texts.
Project Structure
app.py: FastAPI application file where the API and model are initialized.
summarizer.py: Script to fine-tune the model on the chosen dataset.
test_request.py: Script to test the API using a POST request.
requirements.txt: Python dependencies for the project.

