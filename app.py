# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import summarize_text  # Import the summarization function from summarizer.py

# Initialize FastAPI app
app = FastAPI()

# Define the data model for the input
class SummarizationInput(BaseModel):
    prompt: str

# Define the summarization endpoint
@app.post("/summarise")
def summarise(input_data: SummarizationInput):
    try:
        # Summarize the provided text
        summary = summarize_text(input_data.prompt)
        return {"response": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
