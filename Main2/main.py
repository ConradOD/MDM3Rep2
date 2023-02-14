import numpy as np
import pandas as pd

import scenario
import aircraft
import metrics
import parameters
import output
from machine_learning_modular import *

#Variables
args = []
Parameters = parameters.Parameters()
separation_threshold = 5 #Needs redoing


## We are going to contain this within a function so we can loop the scenario and metric functions within the modular ML function

def scenario_metric_modularity(args, Parameters, separation_threshold):

    #Initialise dataframe
    sample_metrics = metrics.Metrics(Parameters,None,None,None,None,None,None)
    sample_output = output.Output(Parameters,None)
    columns = ['scenario_id','pair_id','timestep_id'] + sample_metrics.metric_names + sample_output.output_name
    data = pd.DataFrame(columns=columns)

    #Gather data for each random scenario
    for scenario_index in range(Parameters.num_scenarios):
        #Generate scenario object
        Scenario = scenario.Scenario(Parameters)

        #Generate output labels, for each pair  of planes
        Output = output.Output(Parameters,Scenario)
        Output.make_crashed_dict()

        #Perform the time evolution
        for timestep in range(0,Parameters.num_t_steps,Parameters.t_evo_step_size):
            #Set plane position according to timestep
            Scenario.move_aircraft_along_path(timestep)

            #Calculate metrics for each pair of planes
            for pair_id,pair in Scenario.aircraft_pair_dict.items():
                #Calculate metrics
                ids = [scenario_index,pair_id,timestep]
                Metrics = metrics.Metrics(Parameters,data,Scenario.aircraft_dict[pair[0]],Scenario.aircraft_dict[pair[1]],scenario_index,pair_id,timestep)
                Metrics.calc_all_metrics()

                #Store row in dataframe
                row = {'scenario_id':scenario_index,'pair_id':pair_id,'timestep_id':timestep}
                row.update(Metrics.data_dict)
                row.update({'crashed':Output.crashed_dict[pair_id]})
                data = pd.concat([data,pd.Series(row).to_frame(1).T])

    data = data[data.timestep_id>5]
    return(data)






#--------------------Repeat Machine Learning w/ Scenario Modularity ---------------------------
# Number of scenarios / repeats for each model
number_repeats = 5
single_metric_nested_list = []
all_metric_nested_list = []

for i in range(number_repeats):
    data_input = scenario_metric_modularity(args, Parameters, separation_threshold)
    machine_learning_modular(data_input,single_metric_nested_list,all_metric_nested_list)
    #print(single_metric_nested_list,all_metric_nested_list)
print(single_metric_nested_list,all_metric_nested_list)





#--------------------Plotting Section---------------------------
import matplotlib.pyplot as plt
#Setup 3d plotting
ax = plt.figure().add_subplot(projection='3d')

for key,plane in Scenario.aircraft_dict.items():
    pos = plane.random_path_position
    #For each plane plots line of trajectory
    ax.plot(pos[:,0],pos[:,1],pos[:,2],label="Plane {id}".format(id = plane.id))
    #Dot for start pos
    ax.scatter(pos[0,0],pos[0,1],pos[0,2])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.legend()
plt.show() 

