from scipy import stats
from sklearn.utils import resample
import numpy as np
import pandas as pd


class preprocessing:

    def prepare(df):

        df1 = df.copy()

        train = df1[(df1['Subject'] != 'subject10')]

        test = df1.drop(train.index, axis=0)

        # train.shape, test.shape

        X_train = train.drop(['Activity', 'Subject'], axis=1)
        y_train = train['Activity']
        X_test = test.drop(['Activity', 'Subject'], axis=1)
        y_test = test['Activity']
        # print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

        # function to create time series datset for seuence modeling

        def create_dataset(X, y, time_steps, step=1):
            Xs, ys = [], []
            for i in range(0, len(X) - time_steps, step):
                x = X.iloc[i:(i + time_steps)].values
                labels = y.iloc[i: i + time_steps]
                Xs.append(x)
                ys.append(stats.mode(labels)[0][0])
            return np.array(Xs), np.array(ys).reshape(-1, 1)

        X_train, y_train = create_dataset(X_train, y_train, 80, step=50)
        # X_train.shape, y_train.shape
        X_test, y_test = create_dataset(X_test, y_test, 80, step=50)
        print(df1.Activity.value_counts())
        return X_train, y_train, X_test, y_test
