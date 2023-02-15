# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:14:03 2023

@author: By237Fact
"""

import numpy as np
import pandas as pd

a = np.array([[0,1,1],
              [5,2,3],
              [10,2,45],
              [7,2,30],
              [45,785,3]])


# print(a[::-1,::-1])

# print(np.argsort(a))

b = pd.read_csv("personnes.csv",sep=";")
print(b)
print(round(b.describe(),2))