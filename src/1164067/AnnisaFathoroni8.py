# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:27:05 2019

@author: HP
"""

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(model.summary())