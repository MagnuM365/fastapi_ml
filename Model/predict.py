import pickle
import pandas as pd

def load_model():
    with open("Model/laptop_price_predictor.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)
    return round(prediction[0], 2)
