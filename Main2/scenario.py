import numpy as np
import aircraft

class Scenario:
    def __init__(self,_Parameters):
        self.Parameters = _Parameters

        self.generate_scenario()
        self.make_aircraft_dict()
        self.generate_random_evolution()
        self.make_pair_list()

    def generate_scenario(self):
        self.initial_positions = np.random.rand(self.Parameters.num_aircraft,3) * self.Parameters.grid_size
        self.initial_velocities = np.random.rand(self.Parameters.num_aircraft,3) * 5 #Should be in direction of (end_point - initial_point)
        self.end_points = np.random.rand(self.Parameters.num_aircraft,3) * self.Parameters.grid_size

    def make_aircraft_dict(self):
        self.aircraft_dict = {}
        self.aircraft_ids = []
        for index in range(self.Parameters.num_aircraft):
            self.aircraft_dict[index] = aircraft.Aircraft(index,self.initial_positions[index,:],self.initial_velocities[index,:],self.end_points[index,:])
            self.aircraft_ids.append(index)

    def generate_random_evolution(self):
        for key,Aircraft in self.aircraft_dict.items():
            Aircraft.make_random_path(self.Parameters)
    
    def make_pair_list(self):
        self.aircraft_pair_list = [[x,y] for x in self.aircraft_ids for y in self.aircraft_ids if y>x]


                       

