from scipy import stats
from sklearn.utils import resample
import numpy as np
import pandas as pd


class prepare:

    def prepare(test):
        y_train = np.zeros(len(test))

        def create_dataset(X, y, time_steps, step=1):
            Xs, ys = [], []
            for i in range(0, len(X) - time_steps, step):
                x = X.iloc[i:(i + time_steps)].values
                # labels = y.iloc[i: i + time_steps]
                Xs.append(x)
                # ys.append(stats.mode(labels)[0][0])
            return np.array(Xs), np.array(ys).reshape(-1, 1)

        test, y_train = create_dataset(test, y_train, 100, step=50)
        return test
