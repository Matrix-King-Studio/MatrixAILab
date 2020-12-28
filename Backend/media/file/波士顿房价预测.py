import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def trainTestSplit(X, y, test_size, random_state):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def readCsv(path, header):
    return pd.read_csv(filepath_or_buffer=path, header=header)


if __name__ == '__main__':
    # 读取训练数据集
    trainData = readCsv(r"G:\Project\MatrixAILab\Backend\media\file\train.csv", 0)

    trainData.drop("Id", axis=1, inplace=True)

    # 数据预处理
    na_count = trainData.isnull().sum().sort_values(ascending=False)
    na_rate = na_count / len(trainData)
    na_data = pd.concat([na_count, na_rate], axis=1, keys=['count', 'ratio'])
    trainData.drop(na_data[na_data['count'] > 1].index, axis=1, inplace=True)
    trainData.drop(trainData.loc[trainData['Electrical'].isnull()].index, inplace=True)
    for col in trainData.columns:
        if trainData[col].dtypes == "object":
            trainData[col], uniques = pd.factorize(trainData[col])

    # 训练/测试集划分
    XData, yData = trainData.iloc[:, :-1], trainData.iloc[:, -1]
    X_train, X_test, y_train, y_test = trainTestSplit(XData, yData, 0.33, 42)

    # 线性回归模型
    lr = LinearRegression()

    # 拟合
    lr.fit(X_train, y_train)

    # 评测
    score = lr.score(X_test, y_test)
    print(score)

    # 读取测试数据集
    testData = readCsv(r"G:\Project\MatrixAILab\Backend\media\file\test.csv", 0)

    # 数据预处理
    testID = testData["Id"]
    testData.drop("Id", axis=1, inplace=True)
    testData.drop(na_data[na_data['count'] > 1].index, axis=1, inplace=True)
    for col in testData.columns:
        if testData[col].dtypes == "object":
            testData[col], uniques = pd.factorize(testData[col])
        testData[col].fillna(testData[col].mean(), inplace=True)

    # 预测
    predict = lr.predict(testData)

    # 保存模型
    with open(r"G:\Project\MatrixAILab\Backend\media\file\model.pkl", "wb") as fp:
        pickle.dump(lr, fp)

    submit = pd.concat([testID, pd.Series(abs(predict))], axis=1, keys=["Id", "SalePrice"])
    submit.to_csv(r"G:\Project\MatrixAILab\Backend\media\file\submisson.csv", index=False)
