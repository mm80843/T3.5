import pandas as pd
import os, json

from owlready2 import *



def getNameLabel(x):
    try :
        b = x.label[0]
    except:
        b = str(x)
    return b

