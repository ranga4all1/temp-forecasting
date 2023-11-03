# FastAPI web service for temperature prediction

from fastapi import FastAPI
from prophet import Prophet
from pydantic import BaseModel
from typing import List
import pickle
import pandas as pd


app = FastAPI()


# Function to create date range DataFrame
def create_date_range_dataframe(start_date, end_date):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    date_range = pd.date_range(start=start_date, end=end_date, freq="D")
    df = pd.DataFrame({"ds": date_range})
    return df


class TemperatureForecastRequest(BaseModel):
    start_date: str
    end_date: str


class TemperatureForecastResponse(BaseModel):
    forecast: List[dict]


# Load the saved model
with open("prophet_base_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)


@app.post("/forecast_temperature/")
async def forecast_temperature(request_data: TemperatureForecastRequest):
    try:
        # Call the function to create the DataFrame
        df_future = create_date_range_dataframe(
            request_data.start_date, request_data.end_date
        )

        # Use the loaded model for forecasting
        forecast_future = loaded_model.predict(df_future)

        # Return the forecasted values of interest as a list of dictionaries
        forecast_data = forecast_future[
            ["ds", "yhat", "yhat_lower", "yhat_upper"]
        ].to_dict(orient="records")
        response_data = TemperatureForecastResponse(forecast=forecast_data)
        return response_data
    except ValueError as e:
        return {
            "error": "Invalid date format. Please enter dates in the YYYY-MM-DD format."
        }


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app using uvicorn when this script is executed
    uvicorn.run(app, host="0.0.0.0", port=8080)
