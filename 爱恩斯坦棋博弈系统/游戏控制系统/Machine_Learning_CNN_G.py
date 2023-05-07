import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, optimizers, Sequential

conv_net = Sequential([
    # unit1
    layers.Conv2D(32, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(32, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),
    # unit2
    layers.Conv2D(64, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),
    # unit3
    layers.Conv2D(128, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(128, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),
    # unit4
    layers.Conv2D(500, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(500, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same")
])
fc_net = Sequential([
    layers.Dense(400, activation=tf.nn.relu),
    layers.Dense(200, activation=tf.nn.relu),
    layers.Dense(50, activation=tf.nn.relu),
    layers.Dense(18, activation=None)
])
conv_net.load_weights('.//conv_weight_CNN/')
fc_net.load_weights('.//fc_weight_CNN/')
conv_net.build(input_shape=[None, 5, 5, 3])
fc_net.build(input_shape=[None, 500])

def GetValue(x):
    x = tf.reshape(x, [-1, 5, 5, 3])
    x = tf.cast(x, dtype=tf.float32)
    out = conv_net(x)
    out = tf.reshape(out, [-1, 500])
    logits = fc_net(out)
    prob = tf.nn.softmax(logits, axis=1)
    pred = tf.argmax(prob, axis=1)
    pred = tf.cast(pred, dtype=tf.float32)
    return int(pred)
