import pandas as pd

df = pd.read_csv('../datasets/CommvsCrime.csv')
goodCrime = df['ViolentCrimesPerPop']
badCrime = df['nonViolPerPop']
totalCrime = badCrime + goodCrime
print totalCrime
