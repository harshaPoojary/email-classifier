from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from masking import mask_pii
from classify import classify_email

app = FastAPI()

# Load model
try:
    model = joblib.load("email_classifier.pkl")
    print(" Model loaded successfully")
except Exception as e:
    print(" Model loading failed:", str(e))

class EmailRequest(BaseModel):
    input_email_body: str

@app.post("/classify")
def classify(request: EmailRequest):
    original_email = request.input_email_body

    try:
        print(" Original Email:", original_email)

        # Step 1: Mask
        masked_email, entities = mask_pii(original_email)
        print(" Masked Email:", masked_email)
        print(" Entities:", entities)

        # Step 2: Classify
        category = classify_email(masked_email, model)
        print("🏷 Category:", category)

        return {
            "input_email_body": original_email,
            "list_of_masked_entities": entities,
            "masked_email": masked_email,
            "category_of_the_email": category
        }

    except Exception as e:
        print(" INTERNAL ERROR:", str(e))
        return {"error": "Internal Server Error"}


    except Exception as e:
        print("🔥 INTERNAL ERROR:", str(e))
        return {"error": "Internal Server Error"}
