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
        self.initial_positions = np.random.rand(self.Parameters.num_aircraft,3) * self.Parameters.grid_size + np.array([0,0,self.Parameters.vertical_offset]) 
        self.direction = np.random.rand(self.Parameters.num_aircraft,3) * self.Parameters.velocity_mag
        self.initial_velocities = (self.direction + np.random.rand(self.Parameters.num_aircraft,3) * self.Parameters.direction_variation) * self.Parameters.velocity_mag
        self.initial_acceleration = np.zeros((self.Parameters.num_aircraft,3))

    def make_aircraft_dict(self):
        self.aircraft_dict = {}
        self.aircraft_ids = []
        for index in range(self.Parameters.num_aircraft):
            self.aircraft_dict[index] = aircraft.Aircraft(self.Parameters,index,self.initial_positions[index,:],self.initial_velocities[index,:],self.direction[index,:],self.initial_acceleration[index,:])
            self.aircraft_ids.append(index)

    def generate_random_evolution(self):
        for key,Aircraft in self.aircraft_dict.items():
            Aircraft.make_random_path()
    
    def make_pair_list(self):
        self.aircraft_pair_list = [[x,y] for x in self.aircraft_ids for y in self.aircraft_ids if y>x]


                       

