import pandas as pd
import os
from owlready2 import *

import owlready2


def getNameLabel(x):
    try :
        b = x.label[0]
    except:
        b = str(x)
    return b

