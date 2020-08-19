import numpy as np

from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from sklearn import preprocessing
import keras.backend as K
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = np.loadtxt('data/data.csv', delimiter=',')
    X = data[:, :4]
    Y = data[:, 4:]

    X = preprocessing.scale(X)
    # Y = np_utils.to_categorical(Y)

    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.8, shuffle=True)
    print(train_X.shape, test_X.shape, train_Y.shape, test_Y.shape)

    model = Sequential()
    model.add(Dense(10, activation='sigmoid', input_shape=(4, )))
    model.add(Dense(40,activation='sigmoid'))
    model.add(Dense(20,activation='sigmoid'))
    model.add(Dense(5,activation='sigmoid'))
    model.add(Dense(2,activation='sigmoid'))
    model.add(Dense(1))

    model.compile(optimizer='sgd',
                  loss='mean_squared_error',
                  metrics=['mae'])
    epochs = 1000
    result = model.fit(train_X, train_Y, epochs=epochs, batch_size=10, verbose=0, shuffle=True, validation_data=(test_X, test_Y))
    prediction = model.predict(test_X).flatten()
    print(prediction)
    print(test_Y.flatten())

    loss, accuracy = model.evaluate(test_X, test_Y, verbose=0)
    print("Accuracy = {:.2f}".format(loss))
    plt.plot(range(1, epochs+1), result.history['loss'], label="training")
    plt.plot(range(1, epochs+1), result.history['val_loss'], label="validation")
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
