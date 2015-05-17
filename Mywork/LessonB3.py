import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

dfr = pd.read_csv('../datasets/loanf.csv')
dfr['TF'] = dfr['Interest.Rate'] <= 12
check = dfr[dfr['Interest.Rate'] == 10 ]

# Adding intercept column
dfr['intercept'] = 1.0

# Loading independent variabels
ind_cols = ['FICO.Score','Loan.Amount','intercept']
logit = sm.Logit(dfr['TF'], dfr[ind_cols])
result = logit.fit()
coeff = result.params
Lamount = dfr['Loan.Amount']
fico = 720

# Function to output the probablity of receiving the loan at below 12% interest
def Loanp(fico, amt, coeff):
  # compute the linear expression by multipyling the inputs by their respective coefficients.
  # note that the coefficient array has the intercept coefficient at the end
  z = coeff[0]*fico + coeff[1]*amt + coeff[2]
  return 1/(1 + np.exp( -1 * z))


# Vectorize my function and exclude the 3rd parameter coeff
vLoanp = np.vectorize(Loanp)
vLoanp.excluded.add(2)

# get the probablity for each row 
dfr['probablity'] = vLoanp(fico, Lamount, coeff)

# if its above 2/3 probablity then we can expect to get the loan 
accepted = dfr['probablity'] >= .67


# Wasn't sure how to plot this as a graph, a table would probably better
p = plt.plot(Lamount, accepted)
ax = plt.gca()
xt = ax.set_xlabel('Loan Amount')
yt = ax.set_ylabel('Acceptance')
plt.show()

