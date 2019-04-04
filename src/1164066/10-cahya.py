# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:27:10 2019

@author: ASUS
"""
loss, acc = model.evaluate(test_input, test_labels, batch_size=32)
# In[3]: fitur ektraksi
print("Done!")
print("Loss: %.4f, accuracy: %.4f" % (loss, acc))