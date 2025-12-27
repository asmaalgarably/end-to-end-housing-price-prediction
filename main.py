from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

model = pickle.load(open('train_model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))


app=FastAPI()

class DataHousing(BaseModel):
   longitude: float
   latitude: float
   housing_median_age: float
   total_rooms: float
   total_bedrooms: float
   population: float
   households: float
   median_income: float


@app.post("/predict" ,response_model=None)
def predict_house_data(data: DataHousing):
   input_data=np.array([[data.longitude,
                         data.latitude,
                         data.housing_median_age,data.total_rooms,
                       data.total_bedrooms,data.population,
                       data.households,
                       data.median_income]])
   input_scaler = scaler.transform(input_data)
   pred = model.predict(input_scaler)

   return {"estimated_value": round(float(pred[0]), 2)}

   

