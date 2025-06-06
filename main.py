from fastapi import FastAPI
from fastapi.responses import JSONResponse  
import pandas as pd
from schema.user_input import UserInput 
from Model.predict import predict_output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Laptop Price Prediction API. Use the /predict endpoint to get predictions."} 

@app.get("/health")
def health_check():
    return JSONResponse(status_code=200, content={"status": "OK", "message": "API is running smoothly."})


@app.post("/predict")
def predict_price(user_input: UserInput):
    input_data = {
            'Brand': user_input.Brand,
            'Processor': user_input.Processor,
            'Graphics': user_input.Graphics,
            'Series': user_input.Series,
            'Ram': user_input.Ram,
            'Storage': user_input.Storage
    }

    try:
        prediction = predict_output(input_data)
        return JSONResponse(status_code=200, content={"predicted_price": prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
