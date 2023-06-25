from scipy import stats
from sklearn.utils import resample
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler


class preprocessing:

    def prepare(df):
        # df = df.drop(df[df['Activity'] == 18].index, axis=0)
        # df = df.drop(df[df['Activity'] == 19].index, axis=0)
        X = df.drop(['Time_stamp', 'Subject',
                    'Activity'], axis=1)
        y = df['Activity']
        print(df.Activity.value_counts())
        # oversampler = RandomOverSampler()
        # X, y = oversampler.fit_resample(X, y)
        # print(df.label.value_counts())
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42)

        def create_dataset(X, y, time_steps, step=1):
            Xs, ys = [], []
            for i in range(0, len(X) - time_steps, step):
                x = X.iloc[i:(i + time_steps)].values
                labels = y.iloc[i: i + time_steps]
                Xs.append(x)
                ys.append(stats.mode(labels)[0][0])
            return np.array(Xs), np.array(ys).reshape(-1, 1)

        X_train, y_train = create_dataset(X_train, y_train, 100, step=50)
        X_test, y_test = create_dataset(X_test, y_test, 100, step=50)

        return X_train, y_train, X_test, y_test
