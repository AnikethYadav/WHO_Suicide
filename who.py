import os
os.chdir("/home/aniket/Documents/datasets/WHO_Suicide/")

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
print(os.listdir("../WHO_Suicide"))

country = pd.read_csv('../input/who_suicide_statistics.csv')