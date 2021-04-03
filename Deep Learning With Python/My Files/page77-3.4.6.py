#%% 
import keras 
keras.__version__
# %%
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# %%
train_images.shape
# train_labels.shape
# %%
from keras import models
from keras import layers

# %%
network = models.Sequential()
network.add(layers.Dense(512, activation= 'relu', input_shape= (28*28, )))
network.add(layers.Dense(512, activation= 'relu'))
network.add(layers.Dense(10, activation= 'softmax'))

network.compile(optimizer= 'rmsprop', loss= 'mse', metrics=['accuracy'])

# %%
train_images = train_images.reshape((60000, 784))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 784))
test_images = test_images.astype('float32') / 255

# %%
test_images.shape ,train_images.shape

# %%
train_labels
# %%
from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# %%
train_labels.shape, train_labels
# %%
train_labels[0]
# %%
network.fit(train_images, train_labels, batch_size= 128, epochs= 5)
# %%
test_loss, test_acuracy = network.evaluate(test_images, test_labels)
# %%
test_loss, test_acuracy
# %%
result = network.predict(test_images[0].reshape((1,28*28)))
# %%
test_images[0].plot()
    # %%
