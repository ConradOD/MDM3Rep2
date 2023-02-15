
import pandas as pd

#Read pkl files
#single_metric1 = 
single_metric2 = pd.read_pickle("single_metric2.pkl")
#all_metric1 = 
all_metric2 = pd.read_pickle("all_metric2.pkl")


print(single_metric2.head())
print(all_metric2.head())

#Vars to use for unpacking
num_repeats = 25
metric_names = ['distance','vel_diff','yaw_diff','pitch_diff','shortest_dist_timed','shortest_dist_path','dist_f_expected_path','ratio_distance','ratio_velocity']
combined_name = ['Combined']
column_names = ['repeat'] + metric_names + combined_name
  

#Setup df
df = 

#Extract individually
for repeat in range(num_repeats):
    #Make row of all the metric and then 


#Gonna need to shift one set of files by 25
#Ie repeats 0 becomes repeat 25

#Combine 







'''
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

'''
