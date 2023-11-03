# Model training for - Temperature forcasting - daily temperature in Delhi, India.

print("importing required libraries...")
# import required libraries
import pickle
import numpy as np
import pandas as pd
from prophet import Prophet

print("Loading and preprocessing data...")
# Load the data
df = pd.read_csv("../data/DailyDelhiClimateTrain.csv")

# data pre-processing
df["date"] = pd.to_datetime(df["date"])
df = df.rename(columns={"date": "ds", "meantemp": "y"})


# Function to train the prophet model and save it
def train_and_save_prophet_model():
    print("Prophet model training started...")
    # train prophet model
    base_model = Prophet()
    base_model.fit(df)
    print("Prophet model training completed.")

    # save model
    with open("prophet_base_model.pkl", "wb") as model_file:
        pickle.dump(base_model, model_file)
    print("Prophet model saved as prophet_base_model.pkl")


if __name__ == "__main__":
    train_and_save_prophet_model()
