
import  pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import  matplotlib.pyplot as plt

from collections import Counter

df=pd.read_csv('bankloan.csv')
df=df.dropna()
df.isna().any()
df=df.drop('Loan_ID',axis=1)
df['LoanAmount']=(df['LoanAmount']*1000).astype(int)
pre_Y=df['Loan_Status']
pre_X=df.drop('Loan_Status',axis=1)
#One Hot Encoding
dm_X=pd.get_dummies(pre_X)
dm_Y=pre_Y.map(dict(Y=1,N=0))
#training
x_train,x_test,y_train,y_test=train_test_split(dm_X,dm_Y,test_size=0.2,random_state=42,shuffle=True)

from sklearn import svm

svm=svm.SVC(kernel='linear') # Linear Kernel
svm.fit(x_train, y_train)
y_pred = svm.predict(x_test)

#
from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#
# import pickle
# from sklearn.externals import joblib
# filename='loan_model.pkl'
# joblib.dump(svm,filename)



