import pandas as pd
import matplotlib.pyplot as plt

# Lesson A1 Linear Regression - Overview
# we have to clean up the raw data set which we will do
# in the next lesson. But for now let's look at the cleaned up data.
# import the cleaned up dataset into a pandas data frame
df = pd.read_csv('../datasets/loanf.csv')

# extract FICO Score and Interest Rate and plot them
# FICO Score on x-axis, Interest Rate on y-axis
intrate = df['Interest.Rate']
fico = df['FICO.Score']
p = plt.plot(fico, intrate, 'o')
ax = plt.gca()
xt = ax.set_xlabel('FICO Score')
yt = ax.set_ylabel('Interest Rate %')
plt.show()

# Lesson A2 Linear Regression - Data Exploration
loansData = pd.read_csv('../datasets/loansData.csv')

# functions for converting data


def p2f(x):
  return float(x.strip("%"))/100


def m2i(x):
  return int(x.strip("months"))


def ficoMid(x):
  num1 = int(x[:3])
  num2 = int(x[len(x) - 3:])
  return (num1 + num2)/2

# For iterating over data to filter
def Loanfilter(obj, func):
  temp = obj.copy()
  for key, value in obj.iteritems():
    temp[key] = func(obj[key])
  return temp


# loading into dataFrame with just the parsed information I need
loansParsed = pd.core.frame.DataFrame()

loansParsed['Interest'] = Loanfilter(loansData['Interest.Rate'], p2f)
loansParsed['FICO'] = Loanfilter(loansData['FICO.Range'], ficoMid)
loansParsed['LoanMons'] = Loanfilter(loansData['Loan.Length'], m2i)

print loansParsed[0:3]
