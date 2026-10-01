import pandas as pd

df = pd.read_csv("nobel-prize-laureates.csv")
df = df[["awardYear", "category", "categoryFullName"]]
df.to_csv("nobel-prize-laureates-text_only.csv", index=False)
