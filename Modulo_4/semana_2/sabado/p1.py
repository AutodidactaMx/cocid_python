import pandas as pd
import numpy as np

df = pd.read_csv('london_merged.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df["wind_speed^2"] = df["wind_speed"]**2
df["wind_speed-sin"] = np.sin(df["wind_speed"])
df["diff_t"] = df["t1"] - df["t2"]

df["diff_t_row2"] = df["t1"].iloc[::2].sub(df["t2"], fill_value=0) 

print(df[["diff_t","diff_t_row2"]])