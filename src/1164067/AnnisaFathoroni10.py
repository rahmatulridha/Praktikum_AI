# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:27:55 2019

@author: HP
"""

loss, acc = model.evaluate(test_input, test_labels, batch_size=32)

print("Done!")
print("Loss: %.4f, accuracy: %.4f" % (loss, acc))