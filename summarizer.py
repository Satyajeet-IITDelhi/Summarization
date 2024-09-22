# summarizer.py

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

# Load pre-trained summarization model (BART)
model_name = "facebook/bart-large-cnn"  # You can choose a different summarization model
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text: str) -> str:
    """Summarize the input text."""
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Example usage (Optional, for testing purposes)
if __name__ == "__main__":
    input_text = "Your long text to summarize goes here."
    print("Original Text:", input_text)
    print("Summarized Text:", summarize_text(input_text))
