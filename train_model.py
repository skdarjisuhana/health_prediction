import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = {
    "glucose":[80,90,100,120,140,160,180,200],
    "haemoglobin":[14,13,12,11,10,9,8,7],
    "cholesterol":[150,170,180,200,220,240,260,300],
    "risk":[0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["glucose","haemoglobin","cholesterol"]]
y = df["risk"]

model = DecisionTreeClassifier()
model.fit(X,y)

joblib.dump(model,"health_model.pkl")

print("Model Trained Successfully")