# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:27:10 2019

@author: ASUS
"""
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(model.summary())