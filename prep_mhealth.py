from scipy import stats
from sklearn.utils import resample
import numpy as np
import pandas as pd


class prep_mhealth:

    def prepare(df):
        from sklearn.utils import resample

        df_majority = df[df.Activity == 0]
        df_minorities = df[df.Activity != 0]

        df_majority_downsampled = resample(
            df_majority, n_samples=30000, random_state=42)
        df = pd.concat([df_majority_downsampled, df_minorities])
        df.Activity.value_counts()
        df1 = df.copy()

        for feature in df1.columns[:-2]:
            lower_range = np.quantile(df[feature], 0.01)
            upper_range = np.quantile(df[feature], 0.99)
            print(feature, 'range:', lower_range, 'to', upper_range)

            df1 = df1.drop(df1[(df1[feature] > upper_range) | (
                df1[feature] < lower_range)].index, axis=0)
            print('shape', df1.shape)
        train = df1[(df1['subject'] != 'subject10') &
                    (df1['subject'] != 'subject9')]
        test = df1.drop(train.index, axis=0)
        train.shape, test.shape
        X_train = train.drop(['Activity', 'subject'], axis=1)
        y_train = train['Activity']
        X_test = test.drop(['Activity', 'subject'], axis=1)
        y_test = test['Activity']
        X_train.shape, y_train.shape, X_test.shape, y_test.shape
        from scipy import stats

        # function to create time series datset for seuence modeling
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
