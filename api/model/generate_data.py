import pandas as pd
import numpy as np

data = []

for _ in range(5000):
    distance = np.random.randint(50, 2000)
    speed = np.random.randint(50, 90)
    traffic = np.random.randint(1, 5)
    weather = np.random.randint(1, 5)
    weight = np.random.randint(1000, 30000)

    eta = distance / speed + traffic * 0.3 + weather * 0.4

    data.append([distance, weight, speed, traffic, weather, eta])

df = pd.DataFrame(data, columns=[
    "distance", "weight", "speed", "traffic", "weather", "eta"
])

df.to_csv("dataset.csv", index=False)
