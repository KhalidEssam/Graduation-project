

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from imblearn.over_sampling import RandomOverSampler
from statistics import mode
import joblib


class loader:
    # data = pd.read_csv('E:\MY-GRAD\CNN-LSTM\correct_data.csv')

    # X = data.drop(['Time (s)', 'Magnetometer X (uT)',
    #               'Magnetometer Y (uT)',	'Magnetometer Z (uT)', 'label'], axis=1)
    # y = data['label']
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, test_size=0.2, random_state=42)
    # global loaded_model

    # loaded_model.fit(X_train, y_train)
    # global i
    # i = 0
    global correct_incorrect
    correct_incorrect = ['Correct', 'Correct',
                         'Incorrect', 'Correct',  'Incorrect']

    def Livedemo():
        # print("hiiiii")
        headers = ['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)',
                   'Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)']
        loaded_model = joblib.load('random_forest_model1.h5')
        label_map = {

            0: 'Correct',
            1: 'Incorrect',
        }

        import pandas as pd
        ct = 0
        path = 'E:/MY-GRAD/CNN-LSTM/MYprojectssss.csv'
        Test = pd.read_csv(path)
        header = Test.columns.tolist()
        if header[0] == 'Gyroscope X (deg/s)':
            ct += 1
        else:
            Test.columns = headers

        # Use the loaded model for predictions
        predictions = loaded_model.predict(Test)
        # print(label_map[mode(predictions)])
        print(correct_incorrect[0])
        del correct_incorrect[0]
        # print(correct_incorrect)

        # joblib.dump(loaded_model, 'random_forest_model1.h5')

    # Livedemo('E:/MY-GRAD/CNN-LSTM/MYprojectssss.csv')
