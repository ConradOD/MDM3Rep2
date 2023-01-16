import numpy as np
import pandas as pd
#Import other files
import scenario
import aircraft
import risk
import metrics


#Variables
num_aircraft = 4
grid_size = 10

delta_t = 0.5
max_t = 100
num_t_steps = int(max_t / delta_t)

num_random_paths = 10

num_scenarios = 1   #Num times repeated (different random scenario each time)
#Variables for storing output on each iteration
known_risk = np.zeros(num_scenarios)
unknown_risk = np.zeros(num_scenarios)

#Dataframe for storing output
data = pd.DataFrame([])

#"Make data"
for index in range(num_scenarios):
    #make scenario
    scenario_object = scenario.Scenario(num_aircraft, num_t_steps, grid_size)

    #Initialise metrics
    metric_object = metrics.Metrics(scenario_object)
    for name,val in metric_object.metrics_dict.items():
        data.loc[index,name] = val
    #calc_all_metrics calls all the different metrics functions and dict with key and value for all metrics

    #data[index,'avg_crash'] = risk.calc_known_risk(scenario_object,num_random_paths) #"Known risk"


#Split data
train_data = 0#do this
test_data = 0#do this

print(data.head())

#Train model



#Test model