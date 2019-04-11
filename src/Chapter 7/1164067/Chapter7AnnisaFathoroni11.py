# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:28:34 2019

@author: HP
"""

import keras.callbacks
tensorboard = keras.callbacks.TensorBoard(log_dir='./logs/mnist-style')