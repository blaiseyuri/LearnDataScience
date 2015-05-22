import pandas as pd
samtrain = pd.read_csv('../datasets/samsung/samtrain.csv')
samval = pd.read_csv('../datasets/samsung/samval.csv')
samtest = pd.read_csv('../datasets/samsung/samtest.csv')

# remapping the activity column with names
import randomforests as rf
samtrain = rf.remap_col(samtrain, 'activity')
samval = rf.remap_col(samval, 'activity')
samtest = rf.remap_col(samtest, 'activity')

import sklearn.ensemble as sk

# compute_importances is no longer an option
rfc = sk.RandomForestClassifier(n_estimators=500, oob_score=True)
train_data = samtrain[samtrain.columns[1:-2]]
train_truth = samtrain['activity']
model = rfc.fit(train_data, train_truth)

# estimate of how accurate the model is
print rfc.oob_score_

fi = enumerate(rfc.feature_importances_)
cols = samtrain.columns
print [(value,cols[i]) for (i, value) in fi if value > .04]

val_data = samval[samval.columns[1:-2]]
val_truth = samval['activity']
val_pred = rfc.predict(val_data)

test_data = samtest[samtest.columns[1:-2]]
test_truth = samtest['activity']
test_pred = rfc.predict(test_data)

print("mean accuracy score for validation set = %f" %(rfc.score(val_data, val_truth)))
print("mean accuracy score for test set = %f" %(rfc.score(test_data, test_truth)))

# Confusion matrix shows misclassifications
import sklearn.metrics as skm
test_cm = skm.confusion_matrix(test_truth,test_pred)

# Visualize the confusion matrix
import pylab as pl
pl.matshow(test_cm)
pl.title('Confusion matrix for test data')
pl.colorbar()
pl.show()

# Accuracy
print("Accuracy = %f" %(skm.accuracy_score(test_truth,test_pred)))

# Precision
print("Accuracy = %f" %(skm.precision_score(test_truth,test_pred)))

# Recall
print("Recall = %f" %(skm.recall_score(test_truth,test_pred)))

# F1 Score
print("F1 score = %f" %(skm.f1_score(test_truth,test_pred)))