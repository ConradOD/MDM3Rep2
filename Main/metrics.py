import numpy as np

class Metrics:
    def __init__(self,Scenario):
        self.metrics_dict = {}
        self.scenario = Scenario

        self.calc_avg_dist_between_aircraft()
        #Repeat for all metrics

    def calc_avg_dist_between_aircraft(self):

        num_aircraft = self.Scenario.num_aircraft
        pairwise_distance = np.zeros((num_aircraft,num_aircraft))
        
        for i in range(num_aircraft):
            for j in range(i+1,num_aircraft):
                #Scenario object contains a dictonary containing all the Aircraft objects
                aircraft_i = self.Scenario.aircraft_dict.get(i)
                aircraft_j = self.Scenario.aircraft_dict.get(j)
                
                #Aircraft object contains its own position
                #We use this calculate the distance between 2 aircraft
                distance = np.linalg.norm(aircraft_i.position - aircraft_j.position)
                pairwise_distance[i,j] = distance

        #The metric is stored in the Metrics object dictionary (accessed by main.py)
        self.metrics_dict['avg_pw_dist'] = np.mean(pairwise_distance)
            
