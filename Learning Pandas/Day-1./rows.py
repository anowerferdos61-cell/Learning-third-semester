import pandas as pd


df = pd.read_json('/Users/mac/Desktop/Online Course/Learning Pandas/Day-1./chemistry_data.json')
print(df.head(5))

df = pd.read_json('/Users/mac/Desktop/Online Course/Learning Pandas/Day-1./chemistry_data.json')
print(df.tail(5))