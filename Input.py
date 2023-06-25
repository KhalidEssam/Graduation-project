from xml.etree.ElementInclude import include
from sklearn.metrics import confusion_matrix, classification_report
from scipy import stats
from sklearn.utils import resample
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from prep_mhealth import prep_mhealth as pre
# from CNN_LSTM import Model as CNN_LSTM
from LSTM import Model as CNN_LSTM
# from cnn_gru import Model as CNN_LSTM
# from GRU import Model as CNN_LSTM
from keras.models import load_model
import time
# %matplotlib inline
tf.random.set_seed(42)


label_map = {
    0: 'Nothing',
    1: 'Standing still',
    2: 'Sitting and relaxing',
    3: 'Lying down',
    4: 'Walking',
    5: 'Climbing stairs',
    6: 'Waist bends forward',
    7: 'Frontal elevation of arms',
    8: 'Knees bending (crouching)',
    9: 'Cycling',
    10: 'Jogging',
    11: 'Running',
    12: 'Jump front & back'
}


# label_map = {

#     0: 'Walking',
#     1: 'Crouching',
#     2: 'Running',
#     3: 'Standing',
# }

path = "mhealth_raw_data.csv"
df = pd.read_csv(path)


X_train, y_train, X_test, y_test = pre.prepare(df)
start_time = time.time()
model_lstm = CNN_LSTM.Train(X_train, y_train, X_test, y_test, 10)


end_time = time.time()
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Train Time taken: {elapsed_time} seconds")


start_time = time.time()

pred = CNN_LSTM.Predict(X_test)
pred = np.argmax(pred, axis=1)
pred = pred.reshape(-1, 1)

end_time = time.time()
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Predict Time taken: {elapsed_time} seconds")


print("CNN_lstm_matrix")
print(classification_report(y_test, pred))
print('*'*50)
# print(confusion_matrix(y_test, pred))
plt.figure(figsize=(10, 5))
conf_matrix = confusion_matrix(y_test, pred, normalize='true')
conf_mat_round = np.round(conf_matrix.astype(
    'float')/conf_matrix.sum(axis=1)[:, np.newaxis], decimals=2)
# print(conf_mat_round)
sns.heatmap(conf_mat_round, xticklabels=label_map.values(),
            yticklabels=label_map.values(), annot=True, cmap='Blues', fmt="0.2f")
# plt.title('CNN_GRU model')

plt.show()
