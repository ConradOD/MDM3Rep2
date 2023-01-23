import numpy as np
import pandas as pd

import scenario
import aircraft
import metrics
import parameters

#Variables
args = []
Parameters = parameters.Parameters(num_scenarios=50)
separation_threshold = 5 #Needs redoing

#Initialise dataframe
sample_metrics = metrics.Metrics(Parameters,None,None)
data = pd.DataFrame(columns=sample_metrics.columns)

#Gather data for each random scenario
for scenario_index in range(Parameters.num_scenarios):
    #Generate scenario object
    Scenario = scenario.Scenario(Parameters)

    #For each pair of aircraft
    for pair in Scenario.aircraft_pair_list:
        aircraft_a = Scenario.aircraft_dict[pair[0]]
        aircraft_b = Scenario.aircraft_dict[pair[1]]

        #Calculate metrics
        Metrics = metrics.Metrics(Parameters,aircraft_a,aircraft_b)
        Metrics.calc_all_data()

        #Store row in dataframe
        data = pd.concat([data,Metrics.data_out()])
        # print(Metrics.data_row)

print(data.head())


#------------------Machine learning section-----------------------
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Split the data into test and train sets
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

#Initialise model
model = LinearRegression()

#Train model on train set
model.fit(X_train,y_train)

#Predict using the trained model
y_pred = model.predict(X_test)

#Coefficients of model
print("Coefficients: \n", model.coef_)
#The mean squared error for predictions
print("Mean squared error: %.2f" % mean_squared_error(y_test,y_pred))