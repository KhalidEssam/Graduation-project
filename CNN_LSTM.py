from typing_extensions import Self
import tensorflow as tf
from keras import layers
import keras


class Model:
    model = keras.Sequential()
    model.add(layers.Input(shape=[100, 12]))
    model.add(layers.Conv1D(filters=32, kernel_size=3, padding="same"))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())
    model.add(layers.Conv1D(filters=128, kernel_size=3, padding="same"))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())
    model.add(layers.MaxPool1D(2))
    model.add(layers.LSTM(128))
    model.add(layers.Dropout(0.4))
    model.add(layers.Dense(units=128, activation='relu'))
    model.add(layers.Dense(15, activation='softmax'))
    model.summary()
    # tf.keras.utils.plot_model(model, show_shapes=True)
    callbacks = [keras.callbacks.ModelCheckpoint("CNN_LSTM_4classes.h5", save_best_only=True, monitor="val_loss"),
                 keras.callbacks.EarlyStopping(monitor="val_loss", patience=50, verbose=1)]

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
                  metrics=["sparse_categorical_accuracy"],)

    def Train(X_train, y_train, X_test, y_test, epoch):
        model_history = Model.model.fit(X_train, y_train, epochs=epoch,
                                        validation_data=(X_test, y_test))
        Model.model.save('CNN_LSTM_4classes.h5')

    def Predict(Test_Data):
        # activities = Model.model.predict(Test_Data)
        return Model.model.predict(Test_Data)
