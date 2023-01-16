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

num_scenarios = 5  #Num times repeated (different random scenario each time)

separation_threshold = 5 #distance below which counts as loss of separation.


#Variables for storing output on each iteration
known_risk = np.zeros(num_scenarios)
unknown_risk = np.zeros(num_scenarios)

#Dataframe for storing output
data = pd.DataFrame([])

#"Make data"
for index in range(num_scenarios):
    #make scenario
    scenario_object = scenario.Scenario(num_aircraft, num_t_steps, grid_size, delta_t, separation_threshold)

    #Initialise metrics
    metric_object = metrics.Metrics(scenario_object)
    #This object calculates all the metrics for the scenario and stores them

    #Unpack the metrics into pandas dataframe
    for name,val in metric_object.metrics_dict.items():
        data.loc[index,name] = val


    data.loc[index,'avg_crashed'] = risk.calc_known_risk(scenario_object,num_random_paths)  #Equivalent to known risk

#Split data
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.2,random_state=0)

print(X_train)
print(X_test)

#Train model
from sklearn.linear_model import LinearRegression
classifier = LinearRegression()
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
classifier.fit(X_train,Y_train)
# classification_report()
y_pred = classifier.predict(X_test)
conf_matr = confusion_matrix(Y_test,y_pred)
print(conf_matr)


#Test model