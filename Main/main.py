import numpy as np
import pandas as pd
#Import other files
import scenario
import aircraft
import risk
import metrics


#Variables
num_aircraft = 10
grid_size = 10

delta_t = 0.5
max_t = 100
num_t_steps = int(max_t / delta_t)

num_random_paths = 10

num_scenarios = 5  #Num times repeated (different random scenario each time)


#Variables for storing output on each iteration
known_risk = np.zeros(num_scenarios)
unknown_risk = np.zeros(num_scenarios)

#Dataframe for storing output
data = pd.DataFrame([])

#"Make data"
for index in range(num_scenarios):
    #make scenario
    scenario_object = scenario.Scenario(num_aircraft, num_t_steps, grid_size, delta_t)

    #Initialise metrics
    metric_object = metrics.Metrics(scenario_object)
    #This object calculates all the metrics for the scenario and stores them

    #Unpack the metrics into pandas dataframe
    for name,val in metric_object.metrics_dict.items():
        data.loc[index,name] = val


    data.loc[index,'avg_crashed'] = risk.calc_known_risk(scenario_object,num_random_paths)  #Equivalent to known risk

#Split data
train_data = 0#do this
test_data = 0#do this

print(data.head())

#Train model



#Test model