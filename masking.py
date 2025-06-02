import re
import spacy

nlp = spacy.load("en_core_web_sm")

PII_PATTERNS = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone_number": r"\b(?:\+91[- ]?)?\d{10}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])/?([0-9]{2}|[0-9]{4})\b"
}

def mask_pii(email_text):
    masked_text = email_text
    masked_entities = []

    doc = nlp(email_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            masked_text = masked_text.replace(ent.text, "[full_name]")
            masked_entities.append({
                "position": [email_text.find(ent.text), email_text.find(ent.text) + len(ent.text)],
                "classification": "full_name",
                "entity": ent.text
            })

    for label, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, masked_text):
            entity = match.group()
            masked_text = masked_text.replace(entity, f"[{label}]")
            masked_entities.append({
                "position": [match.start(), match.end()],
                "classification": label,
                "entity": entity
            })

    return masked_text, masked_entities
