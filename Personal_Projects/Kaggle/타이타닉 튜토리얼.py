import pandas as pd
import os

train_data = pd.read_csv('C:/Users/yth21/Desktop/TH/data/Kaggle/Titanic Tutorials/train.csv')
train_data.head()
test_data = pd.read_csv('C:/Users/yth21/Desktop/TH/data/Kaggle/Titanic Tutorials/test.csv')
test_data.head()

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women) / len(women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men) / len(men)

print(rate_women)
print(rate_men)
