import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Rahul"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)