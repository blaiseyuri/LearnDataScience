import pandas as pd
import numpy as np

df = pd.read_csv('../datasets/UCI HAR Dataset/cleandedData.csv', header=0)

# Replace Activity with number values
map_dict = {'LAYING':6, 'SITTING':4, 'STANDING':5, 'WALKING':1, 'WALKING_UPSTAIRS':2, 'WALKING_DOWNSTAIRS':3} 
df['Activity'] = df['Activity'].map(lambda x: map_dict[x])

# Get Subjects so they can be called by their order
subjects = np.unique(df['Subject'])

# Training, validation, and testing sets are seperated by subject
train = df[df.Subject.isin(subjects[:12])]
validation = df[df.Subject.isin(subjects[12:-4])]
test = df[df.Subject.isin(subjects[-4:])]

import sklearn.ensemble as sk

rfc = sk.RandomForestClassifier(n_estimators=500, oob_score=True)
train_data = train.iloc[:,2:]
train_value = train.iloc[:, 1]
model = rfc.fit(train_data, train_value)

print rfc.oob_score_

fi = enumerate(rfc.feature_importances_)
cols = train.columns
print [(value,cols[i]) for (i,value) in fi]

