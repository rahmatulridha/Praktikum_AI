# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:32:10 2019

@author: HP
"""

import keras.models
model2 = keras.models.load_model("mathsymbols.model")
print(model2.summary())