FROM python:3.9-slim

WORKDIR /app
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y gcc g++ build-essential

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

#  Download spaCy model
RUN python -m spacy download en_core_web_sm

# Start the FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
