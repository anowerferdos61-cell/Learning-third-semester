import pandas as pd

data = pd.read_json("chemistry_data.json")
print(data.info())