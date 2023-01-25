import numpy as np
import pandas as pd
#Import other files
import scenario
import aircraft
import risk
import metrics
from sklearn.model_selection import train_test_split

#Variables
num_aircraft = 4
grid_size = 10

delta_t = 0.5
max_t = 10
num_t_steps = int(max_t / delta_t)

num_random_paths = 5

num_scenarios = 20  #Num times repeated (different random scenario each time)

separation_threshold = 5 #Distance below which counts as loss of separation.

#Dataframe for storing output
metric_names = ['avg_pw_dist']  #Update this manually atm
output_name = ['crashed']  #Name of output variable "y"
data = pd.DataFrame(columns=metric_names+output_name)  #Initialising dataframe with column names

#"Make data"
for index in range(num_scenarios):
    #Generate scenario
    scenario_object = scenario.Scenario(num_aircraft, num_t_steps, grid_size, delta_t, separation_threshold)

    #Initialise metrics
    metric_object = metrics.Metrics(scenario_object) #This object calculates all the metrics for the scenario and stores them

    crashed_list = risk.calc_known_risk(scenario_object,num_random_paths)

    for entry in crashed_list:
        new_row = metric_object.metrics_dict
        new_row.update({'crashed':entry})
        new_row = pd.Series(new_row)
        data = pd.concat([data,new_row.to_frame(1).T])

print(data.head(6))

#Split data
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


#Import sklearn functions
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#Initialise linear regression model
model = LinearRegression()

#Train model on train set
model.fit(X_train,y_train)

#Predict using the trained model
y_pred = model.predict(X_test)

#Coefficients of model
print("Coefficients: \n", model.coef_)
#The mean squared error for predictions
print("Mean squared error: %.2f" % mean_squared_error(y_test,y_pred))
#The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))
