import time
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.kernel_ridge import KernelRidge
import matplotlib.pyplot as plt

#Reading data
dataset = pd.read_csv('Sales_Transactions_Dataset_Weekly.csv')
print (dataset)
print(dataset.shape)

#Only normalised data into consideration
data=dataset[dataset.columns[55:]]
print(data)
print(data.shape)

#Splitting dataset into test and train
from sklearn.model_selection import train_test_split
y = data['Normalized 51']
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.3)

#SVR model training
train_size = 790
svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1),param_grid={"C": [1e0, 1e1, 1e2, 1e3],"gamma": np.logspace(-2, 2, 5)})

#SVR model fitting
t0 = time.time()
svr.fit(X_train, y_train)
svr_fit = time.time() - t0
print("SVR complexity and bandwidth selected and model fitted in %.3f s"% svr_fit)

#verification of data dimension
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Predicting using SVR model
result=svr.predict(X_test)
print(result)

#predicted output and test data comparison
temp = zip(result, y_test)
df=[i for i in temp]
print(df)

# Mean Square Error calculation
sum = 0
for i,j in zip(result, y_test):
    sum+= (i-j)**2
    
sum = sum/len(y_test)
print("The MSE of SVR mode is:", sum)


