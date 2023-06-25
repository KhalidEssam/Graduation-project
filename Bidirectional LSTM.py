from typing_extensions import Self
import tensorflow as tf
from keras import layers
import keras


class Model:
    model = keras.Sequential()
    model.add(layers.Bidirectional(layers.LSTM(
        units=50, return_sequences=True, input_shape=[100, 3])))
    model.add(layers.LSTM(units=50, return_sequences=True))
    # Dropout layer
    model.add(layers.Dropout(0.2))
    # Dense layer with ReLu
    model.add(layers.LSTM(units=50, return_sequences=True))
    model.add(layers.Dropout(0.2))
    model.add(layers.LSTM(units=50))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(units=20, activation='softmax'))

    callbacks = [keras.callbacks.ModelCheckpoint("BIDir_4classes.h5", save_best_only=True, monitor="val_loss"),
                 keras.callbacks.EarlyStopping(monitor="val_loss", patience=50, verbose=1)]

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
                  metrics=["sparse_categorical_accuracy"],)

    def Train(X_train, y_train, X_test, y_test, epoch):
        model_history = Model.model.fit(X_train, y_train, epochs=epoch,
                                        validation_data=(X_test, y_test))
        Model.model.save('BIDir_4classes.h5')

    def Predict(Test_Data):
        # activities = Model.model.predict(Test_Data)
        return Model.model.predict(Test_Data)
