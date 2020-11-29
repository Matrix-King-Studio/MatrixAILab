import pandas as pd

df = pd.read_csv(r"G:\Project\MatrixAILab\Backend\media\file\train.csv")
print(df)

columns = [{
    "title": item,
    "dataIndex": item,
    "key": item,
} for item in df.columns.values]
print(columns)

data = []
for item in df.values:
    tmp = {"key": item[0]}
    for i in range(len(columns)):
        tmp[columns[i]["dataIndex"]] = item[i]
    data.append(tmp)
print(data[:5])
