import numpy as np

#Import other files
import initial_scenario
import aircraft
import risk


#Variables
num_planes = 4
grid_size = 10

delta_t = 0.5
max_t = 100
num_t_steps = int(max_t / delta_t)


#Make initial scenario....
[initial_positions, initial_velocities, end_points] = initial_scenario.generate_scenario(num_planes,grid_size)

#Random initial pos and direction etc
#Random start & end points

#Initialise aircraft objects in dict
aircraft_dict = {}
for i in range(num_planes):
    #Generate arrays for initialising the Aircraft objects.=
    pos_array = np.zeros((num_t_steps,3))
    pos_array[0,:] = initial_positions[i,:]
    vel_array = np.zeros((num_t_steps,3))
    vel_array[0,:] = initial_velocities[i,:]

    #Call Aircraft class and stores instances in dict
    aircraft_dict[i] = aircraft.Aircraft(i,pos_array,vel_array,end_points[i,:])

    #Generate "known" paths from initial scenario
    aircraft_dict[i].generate_known_path(delta_t,num_t_steps)

print(aircraft_dict[1].position)
#Calculate known risk from paths


#Calculate unknown risk from 


#Compare or something