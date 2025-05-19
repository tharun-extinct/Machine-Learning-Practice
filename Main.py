# AIM: Demonstration and Implementation of Shallow Architecture using Python, TensorFlow and Keras

import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential

model=Sequential([
  	Dense(2, activation="relu", name="layer1"),
  	Dense(64, activation="relu", name="layer2"),
  	Dense(1, name="layer3")]
)

x=tf.ones([1,2])
y=model(x)

print('the y is',y)
