# Email Classification & PII Masking System 

It classifies incoming support emails into categories like Billing Issues, Technical Support, etc., while masking Personally Identifiable Information (PII) and PCI-sensitive details.



##  Features

PII Detection & Masking (Regex & spaCy-based, **no LLMs** used)
Email Classification into 4 classes: `Incident`, `Request`, `Change`, `Problem`
Deployed as a FastAPI-based API on Hugging Face Spaces
Compliant with Akaike’s required input/output API schema



## How It Works

1. **Input Email →**
2. **PII Masking Applied** (`email`, `credit card`, etc.)
3. **Masked Email Passed to Classifier**
4. **Predicted Category Returned**
5. **Output includes masked version + entity list + classification**



## Files in This Repo

| File | Purpose |
|------|---------|
| `app.py` | FastAPI app exposing `/classify` endpoint |
| `masking.py` | Handles all PII masking logic |
| `classify.py` | Loads model and predicts class |
| `email_classifier.pkl` | Pre-trained classification model |
| `requirements.txt` | Dependencies |
| `Dockerfile` | Container setup for Hugging Face deployment |



##  API Endpoint

**Live Endpoint**:  
[https://harshavardhanpoojary-email-classifier-api-v2.hf.space/classify](https://harshavardhanpoojary-email-classifier-api-v2.hf.space/classify)



### Input Format and  Output Format

```json
{
  "input_email_body": "Your support email content"
}


## Output Format

```json
{
  "input_email_body": "string containing the email",
  "list_of_masked_entities": [
    {
      "position": [start_index, end_index],
      "classification": "entity_type",
      "entity": "original_entity_value"
    }
  ],
  "masked_email": "string containing the masked email",
  "category_of_the_email": "string containing the class"
}
```

