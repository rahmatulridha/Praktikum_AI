# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:19:21 2019

@author: HP
"""

import random
random.shuffle(imgs)
split_idx = int(0.8*len(imgs))
train = imgs[:split_idx]
test = imgs[split_idx:]