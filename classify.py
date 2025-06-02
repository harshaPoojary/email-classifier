import joblib

def classify_email(text, model):
    # If it's a scikit-learn model (RandomForest, SVM etc.)
    return model.predict([text])[0]
