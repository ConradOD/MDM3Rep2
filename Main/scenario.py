import numpy as np
import aircraft

class Scenario:
    def __init__(self,_num_aircraft,_num_t_steps,_grid_size):
        self.num_aircraft = _num_aircraft
        self.num_t_steps = _num_t_steps
        self.grid_size = _grid_size
        [self.initial_positions,self.initial_velocities,self.end_points] = self.generate_scenario()
        self.aircraft_dict = self.make_aircraft_dict()

        pass
        '''
        Input vars like num_planes, delta_t etc
        What attrs do we need?
        Could have:
        List/dict of plane objects
        Different no. of crashed on paths
        Avg no. crashed across paths

        How to handle different random paths?
        '''

    def generate_scenario(self):
        '''
        '''

        initial_positions = np.random.rand(self.num_aircraft,3) * self.grid_size
        initial_velocities = np.random.rand(self.num_aircraft,3)
        end_points = np.random.rand(self.num_aircraft,3) * self.grid_size

        return [initial_positions, initial_velocities, end_points]

    def make_aircraft_dict(self):
        out = {}
        for i in range(self.num_aircraft):
            #Generate arrays for initialising the Aircraft objects.=
            pos_array = np.zeros((self.num_t_steps,3))
            pos_array[0,:] = self.initial_positions[i,:]
            vel_array = np.zeros((self.num_t_steps,3))
            vel_array[0,:] = self.initial_velocities[i,:]

            #Call Aircraft class and stores instances in dict
            out[i] = aircraft.Aircraft(i,pos_array,vel_array,self.end_points[i,:])

        return out


    def generate_random_path(self,):
        pass