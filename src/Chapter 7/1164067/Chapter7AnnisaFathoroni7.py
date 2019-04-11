# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:25:46 2019

@author: HP
"""

onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoder.fit(integer_encoded)