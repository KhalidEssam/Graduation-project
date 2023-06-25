from typing_extensions import Self
import tensorflow as tf
from keras import layers
import keras


class Model:
    model = keras.Sequential()

    # input_shape = 50, 3
    model.add(layers.GRU(units=128, input_shape=[100, 12]))
# Dropout layer
    model.add(layers.Dropout(0.4))
    # model.add(layers.GRU(4, return_sequences=True, return_state=True))
    # Dense layer with ReLu
    model.add(layers.Dense(units=64, activation='relu'))
    # Softmax layer
    model.add(layers.Dense(13, activation='softmax'))

    callbacks = [keras.callbacks.ModelCheckpoint("LSTM_4classes.h5", save_best_only=True, monitor="val_loss"),
                 keras.callbacks.EarlyStopping(monitor="val_loss", patience=50, verbose=1)]

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
                  metrics=["sparse_categorical_accuracy"],)

    def Train(X_train, y_train, X_test, y_test, epoch):
        model_history = Model.model.fit(X_train, y_train, epochs=epoch,
                                        validation_data=(X_test, y_test))
        Model.model.save('LSTM_4classes.h5')

    def Predict(Test_Data):
        # activities = Model.model.predict(Test_Data)
        return Model.model.predict(Test_Data)
