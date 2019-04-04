# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:25:14 2019

@author: HP
"""

model = Sequential([
    Dense(100, input_dim=np.shape(train_input)[1]),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
    ])