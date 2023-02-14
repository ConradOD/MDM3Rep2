
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

import pandas as pd
import numpy as np
import metrics

def machine_learning_modular(data,single_metric_nested_list,all_metric_nested_list):

    #Deal with imbalanced data
    data_0 = data[data.crashed == 0]
    count_0 = data_0.shape[0]

    data_1 = data[data.crashed == 1]
    count_1 = data_1.shape[0]



    if count_0 <= count_1 :

    #Undersample the majority class (not crashed) so classes are balance

    elif count_1 >= count_0:
        data_0_undersampled = data_0.sample(count_1)
        undersampled_df = pd.concat([data_0_undersampled,data_1],axis=0)

    df = undersampled_df

    #Split the data into test and train sets
    X = df.iloc[:,3:-1]
    y = df.iloc[:,-1]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    #--------------------------- FOR EACH INDIVIDUAL METRIC--------------------------------
    sample_metrics = metrics.Metrics(None, None, None, None, None, None, None)
    metric_names = sample_metrics.metric_names

    num_metrics = len(metric_names)

    #print(len(metric_names))
    single_metric_nested_list = []

    for metric in metric_names:

        #Get data corresponding to individual metric
        metric_X_train = X_train.loc[:,metric].values.reshape(-1,1)
        metric_X_test = X_test.loc[:,metric].values.reshape(-1,1)

        #Make regression model
        metric_model = LogisticRegression()
        metric_model.fit(metric_X_train,y_train)

        #Make predictions on test set
        metric_y_pred = metric_model.predict(metric_X_test)

        #Output confusion matrix
        conf_matrix =  confusion_matrix(y_test,metric_y_pred)
        acc_score = accuracy_score(y_test,metric_y_pred)

        #print('Metric: ',metric)
        #print(conf_matrix)
        single_metric_nested_list.append([metric,conf_matrix,acc_score])

    #--------------------------- FOR ALL THE METRICS TOGETHER-------------------------------

    #Initialise model
    model = LogisticRegression()

    #Train model on train set
    model.fit(X_train,y_train)

    #Predict using the trained model
    y_pred = model.predict(X_test)
    #Scores
    acc_score_all = accuracy_score(y_test,y_pred)
    conf_matrix_all = confusion_matrix(y_test,y_pred)
    all_metric_nested_list.append([acc_score_all,conf_matrix_all])


    #Output stuff
    print("Coefficients: \n", model.coef_)
    print("Accuracy score: %.2f" % accuracy_score(y_test,y_pred))

    print("Classification report: ")
    print(classification_report(y_test,y_pred))
    print("Confusion matrix: ")
    print(confusion_matrix(y_test,y_pred))
    return(single_metric_nested_list,all_metric_nested_list)

