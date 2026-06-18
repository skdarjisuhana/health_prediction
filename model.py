import joblib

model = joblib.load("health_model.pkl")

def predict_health(glucose,
                   haemoglobin,
                   cholesterol):

    prediction = model.predict([
        [glucose,
         haemoglobin,
         cholesterol]
    ])

    if prediction[0] == 1:
        return "High Risk of Diabetes/Cardiac Disease"
    else:
        return "Healthy"