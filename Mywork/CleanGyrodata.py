


# This File is for cleaning the three files in the root of the train folder of the
# UCI HAR Dataset and cleaning the column names which are in the features.txt file in the root

import re
import pandas as pd

# column names except for activity
f = open('../datasets/UCI HAR Dataset/features.txt', 'r+')
columns = f.read()
columns = re.split(r'\n', columns)

# Subject Values
f = open('../datasets/UCI HAR Dataset/train/subject_train.txt', 'r+')
srows = f.read()
srows = re.split(r'\n', srows)

# Activity values
f = open('../datasets/UCI HAR Dataset/train/y_train.txt', 'r+')
yrows = f.read()
yrows = re.split(r'\n', yrows)

# All other values
f = open('../datasets/UCI HAR Dataset/train/x_train.txt', 'r+')
xrows = f.read()
xrows = re.split(r'\n', xrows)


n = 0

# replacing numbers with actual activity 
for r in yrows:
  yrows[n] = re.sub(r'1', 'WALKING', yrows[n])
  yrows[n] = re.sub(r'2', 'WALKING_UPSTAIRS', yrows[n])
  yrows[n] = re.sub(r'3', 'WALKING_DOWNSTAIRS', yrows[n])
  yrows[n] = re.sub(r'4', 'SITTING', yrows[n])
  yrows[n] = re.sub(r'5', 'STANDING', yrows[n])
  yrows[n] = re.sub(r'6', 'LAYING', yrows[n])
  n += 1


i = 0
# cleaning the data; removing line numbers, '()','-',',' and repeating words
for col in columns:
  columns[i] = re.sub(r'(\d* )|(\()|(\))','', columns[i])
  columns[i] = re.sub(r',','-', columns[i])
  columns[i] = re.sub(r'-','.', columns[i])
  columns[i] = re.sub(r'\b[a-z](\w+)(\1)+', r'\1', columns[i])
  i += 1



# code pulled from stackover flow question 480214 to remove duplicates
# Doesn't seem like there are any duplicates though
from collections import OrderedDict
list(OrderedDict.fromkeys(columns))

# remove empty values
columns = filter(None, columns)
yrows = filter(None, yrows)
srows = filter(None, srows)

# created data frames with column values
sdf = pd.DataFrame(srows, None, ['Subject'])
ydf = pd.DataFrame(yrows, None, ['Activity'])
xdf = pd.DataFrame(xrows)
xdf = pd.DataFrame(filter(None, xdf[0].str.split().tolist()), None , columns)

# combined the two data frames
df = pd.concat([sdf, ydf, xdf], axis=1)

# convert from scientific notation
df = df.convert_objects(convert_numeric=True)

# output all data as csv file
df.to_csv('../datasets/UCI HAR Dataset/cleandedData.csv', index=False)

