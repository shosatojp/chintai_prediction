import numpy as np

from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from sklearn import preprocessing
import keras.backend as K

if __name__ == "__main__":
    data = np.loadtxt('data/data.csv', delimiter=',')
    X = data[:, :4]
    Y = data[:, 4:]

    X = preprocessing.scale(X)
    # Y = np_utils.to_categorical(Y)

    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.8, shuffle=False)
    print(train_X.shape, test_X.shape, train_Y.shape, test_Y.shape)

    model = Sequential()
    model.add(Dense(4, input_shape=(4, )))
    # model.add(Activation('tanh'))
    model.add(Dense(2))
    # model.add(Activation('tanh'))
    model.add(Dense(1))
    # model.add(Activation('softmax'))
    model.add(Activation('relu'))

    model.compile(optimizer='sgd',
                  loss='mean_squared_error',
                  metrics=['mae'])

    model.fit(train_X, train_Y, epochs=50, batch_size=1, verbose=0, shuffle=False)
    prediction = model.predict(test_X).flatten()
    print(prediction)

    loss, accuracy = model.evaluate(test_X, test_Y, verbose=0)
    print("Accuracy = {:.2f}".format(accuracy))
