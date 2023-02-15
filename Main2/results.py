import numpy as np
import pandas as pd

#Read pkl files
single_metric1 = pd.read_pickle('Main2\\single_metric.pkl')
single_metric2 = pd.read_pickle('Main2\\single_metric2.pkl')
all_metric1 = pd.read_pickle('Main2\\all_metric.pkl')
all_metric2 = pd.read_pickle('Main2\\all_metric2.pkl')

# print(single_metric1.head())
# print(all_metric1.head())

#Vars to use for unpacking
num_repeats = 25
metric_names = ['distance','vel_diff','yaw_diff','pitch_diff','shortest_dist_timed','shortest_dist_path','dist_f_expected_path','ratio_distance','ratio_velocity']
combined_name = ['combined']
column_names = ['repeat'] + metric_names + combined_name
  

#Function for unpacking
def unpack_to_df(single_metrics_df,all_metrics_df,offset):
    df = pd.DataFrame(columns= column_names)
    for repeat in range(num_repeats):
        df_index = repeat + offset
        row = {'repeat':df_index}
        for metric_name in metric_names:
            key_search = metric_name + str(repeat)
            row[metric_name] = single_metrics_df.loc[key_search]
        row['combined'] = all_metrics_df.loc['Combined_'+str(repeat)]
        df = pd.concat([df,pd.Series(row).to_frame(1).T])
    return df

#Call function on each set of data
df1 = unpack_to_df(single_metric1,all_metric1,0)
df2 = unpack_to_df(single_metric2,all_metric2,25)

#Combine outputs
all_df = pd.concat([df1,df2])
# print(all_df)

#Turn df into arrays foor f1 & acc
def turn_column_into_2arrays(df,column_name):
    column = df.loc[:,column_name]
    num_rows = column.size
    accuracy_array = np.zeros(num_rows)
    f1_array = np.zeros(num_rows)

    for index,val in column.items():
        f1_array[index] = val[0]
        accuracy_array[index] = val[1]

    return [f1_array,accuracy_array]


[test1,test2] = turn_column_into_2arrays(all_df,'combined')







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
