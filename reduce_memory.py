# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:01:58 2019

@author: CAI
"""

import pandas as pd
import numpy as np


def reduce_memory(data):
    for i in data.columns:
        if data[i].dtypes == 'int64':
                m = data[i].max()
                n = data[i].min()
                if n >= 0:
                    if m <= 255:
                        data[i] = data[i].astype('uint8')
                    elif m <= 65535 :
                        data[i] = data[i].astype('uint16')
                    elif m <= 4294967295:
                        data[i] = data[i].astype('uint32')
                    else :
                        data[i] = data[i].astype('uint64')
                else :
                    if m <= 127:
                        data[i] = data[i].astype('int8')
                    elif m <= 32767 :
                        data[i] = data[i].astype('int16')
                    elif m <= 2147483647:
                        data[i] = data[i].astype('int32')
                    else :
                        data[i] = data[i].astype('int64')
        if data[i].dtypes == 'float64':
            data[i] = pd.to_numeric(data[i],downcast='float',errors='ignore')


            
    return data
