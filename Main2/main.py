import numpy as np
import pandas as pd

import scenario
import aircraft
import metrics
import parameters
import output

#Variables
args = []
Parameters = parameters.Parameters()
separation_threshold = 5 #Needs redoing

#Initialise dataframe
sample_metrics = metrics.Metrics(Parameters,None,None)
data = pd.DataFrame(columns=sample_metrics.columns)

#Gather data for each random scenario
for scenario_index in range(Parameters.num_scenarios):
    #Generate scenario object
    Scenario = scenario.Scenario(Parameters)

    #Generate path that planes follow. Do planes follow the random path that's used for the output??

    #Generate output labels, for each pair  of planes
    crashed_dict = output.calculate_output

    #Perform the time evolution
    for time in timesteps:
        #Set plane position according to timestep

        #Calculate metrics for each pair of planes
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
import matplotlib.pyplot as plt
#Setup 3d plotting (not sure if this is best way of doing it)
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

#Bounding plot to grid size set
#NOTE: planes might disappear off edge
# ax.set_xlim(0,grid_size)
# ax.set_ylim(0,grid_size)
# ax.set_zlim(0,grid_size)

ax.legend()
plt.show()


#------------------Machine learning section-----------------------
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

#Split the data into test and train sets
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#Initialise model
model = LogisticRegression()

#Train model on train set
model.fit(X_train,y_train)

#Predict using the trained model
y_pred = model.predict(X_test)

#Coefficients of model
print("Coefficients: \n", model.coef_)
#The mean squared error for predictions
# print("Mean squared error: %.2f" % mean_squared_error(y_test,y_pred))

print("Accuracy score: %.2f" % accuracy_score(y_test,y_pred))

print("Classification report: ")
print(classification_report(y_test,y_pred))
print("Confusion matrix: ")
print(confusion_matrix(y_test,y_pred))

print("y_test val counts")
print(y_test.value_counts())

print("y_pred val counts")
print(np.unique(y_pred,return_counts=True))
print(np.unique(y_pred))