import pandas as pd
import numpy as np
import metrics

#Metric names
sample_metrics = metrics.Metrics(None,None,None,None)
metric_names = sample_metrics.metric_names
print(metric_names)
#Import dataframe from file
data = pd.read_pickle('Main2\DataFrame.pkl')
print(data.head())


#------------------Machine learning section-----------------------
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


#Deal with imbalanced data
data_0 = data[data.crashed == 0]
count_0 = data_0.shape[0]

data_1 = data[data.crashed == 1]
count_1 = data_1.shape[0]

print('No. no crash: %0d, No. crash: %0d' % (count_0,count_1))

#Undersample the majority class (not crashed) so classes are balanced 
data_0_undersampled = data_0.sample(count_1)
undersampled_df = pd.concat([data_0_undersampled,data_1],axis=0)

df = undersampled_df

#Split the data into test and train sets
X = df.iloc[:,3:-1]
y = df.iloc[:,-1]
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

#--------------Feature Importance-----------------
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
r = permutation_importance(model, X_test,y_test,n_repeats=30,random_state=0)
importance = r.importances_mean
for i,v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i,v))

# plt.bar([x for x in range(len(importance))], importance)
plt.bar(metric_names, importance)
plt.show()