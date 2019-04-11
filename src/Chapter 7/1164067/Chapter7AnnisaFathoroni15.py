# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:30:29 2019

@author: HP
"""

model.fit(np.concatenate((train_input, test_input)),
          np.concatenate((train_output, test_output)),
          batch_size=32, epochs=10, verbose=2)