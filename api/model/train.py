from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import pandas as pd

df = pd.read_csv("model/dataset.csv")

X = df.drop("eta", axis=1)
y = df["eta"]

model = RandomForestRegressor()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("🎉 Training completed successfully")
