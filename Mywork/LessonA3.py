import pylab as pl
import numpy as np
#from sklearn import datasets, linear_model
import pandas as pd
import statsmodels.api as sm

# import the cleaned up dataset
df = pd.read_csv('../datasets/loanf.csv')

intrate = df['Interest.Rate']
loanamt = df['Loan.Amount']
fico = df['FICO.Score']

# prepping data for the normalize equantion
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#joins the two matrices
x = np.column_stack([x1, x2])

X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared