import numpy as np
import pandas as pd
#Import other files
import scenario
import aircraft
import risk


#Variables
num_aircraft = 4
grid_size = 10

delta_t = 0.5
max_t = 100
num_t_steps = int(max_t / delta_t)

num_scenarios = 1   #Num times repeated (different random scenario each time)
#Variables for storing output on each iteration
known_risk = np.zeros(num_scenarios)
unknown_risk = np.zeros(num_scenarios)

#Dataframe for storing output
data = pd.DataFrame([])


for index in range(num_scenarios):
    #make scenario
    scen = scenario.Scenario(num_aircraft, num_t_steps, grid_size)
    




    data['mean_dist'] = scenario.calc_metrics()

    data['avg_crash'] = 0
    #store output (dataframe)