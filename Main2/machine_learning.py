import pandas as pd
import numpy as np


#Import dataframe from file
data = pd.read_pickle('DataFrame.pkl')
print(data.head())


#------------------Machine learning section-----------------------
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


#Deal with imbalanced data


#Split the data into test and train sets
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#Initialise model
model = LogisticRegression()

#Train model on train set
model.fit(X_train,y_train)

#Predict using the trained model
y_pred = model.predict(X_test)

#Output stuff 
print("Coefficients: \n", model.coef_)
print("Accuracy score: %.2f" % accuracy_score(y_test,y_pred))

print("Classification report: ")
print(classification_report(y_test,y_pred))
print("Confusion matrix: ")
print(confusion_matrix(y_test,y_pred))

print("y_test val counts")
print(y_test.value_counts())

print("y_pred val counts")
print(np.unique(y_pred,return_counts=True))
print(np.unique(y_pred))