 # pulling data from UCI Machine Learning Repository to learn about different factors for crime
 # will be using what was learned from lesson A3
 # may also try Gradient Descent technique from CourseEra Standford Machine Learning course
 # data set can be found here https://archive.ics.uci.edu/ml/datasets/Communities+and+Crime

import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../datasets/CommvsCrime.csv')

blackPercent = df['racepctblack:']
murdPerPop = df['murdPerPop:']

p = plt.plot(blackPercent, murdPerPop, 'o')
ax = plt.gca()
xt = ax.set_xlabel('Black Percentage')
yt = ax.set_ylabel('Murder per 100k pop')
plt.show()
