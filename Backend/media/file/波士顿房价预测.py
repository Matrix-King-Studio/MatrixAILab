import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def trainTestSplit(X, y, test_size, random_state):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def readCsv(path, header):
    return pd.read_csv(filepath_or_buffer=path, header=header)


if __name__ == '__main__':
    trainData = readCsv("train.csv", 0)

    X_train, X_test, y_train, y_test = trainTestSplit(trainData[:, :-1], trainData[:, -1], 0.33, 42)

    lr = LinearRegression()

    lr.fit(X_train, y_train)

    score = lr.score(X_test, y_test)

    testData = readCsv("test.csv", 0)

    predict = lr.predict(testData)
