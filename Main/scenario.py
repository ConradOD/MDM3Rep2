import numpy as np
import aircraft
import metrics




class Scenario:
    def __init__(self,_num_aircraft,_num_t_steps,_grid_size,_delta_t,_separation_threshold):
        self.num_aircraft = _num_aircraft
        self.num_t_steps = _num_t_steps
        self.grid_size = _grid_size
        self.delta_t = _delta_t
        self.separation_threshold = _separation_threshold
        [self.initial_positions,self.initial_velocities,self.end_points] = self.generate_scenario()
        self.aircraft_dict = self.make_aircraft_dict()

        #Generate random paths
        self.current_path = None

    def generate_scenario(self):

        initial_positions = np.random.rand(self.num_aircraft,3) * self.grid_size
        initial_velocities = np.random.rand(self.num_aircraft,3) * 5 #Should be in direction of (end_point - initial_point)
        end_points = np.random.rand(self.num_aircraft,3) * self.grid_size

        return [initial_positions, initial_velocities, end_points]

    def make_aircraft_dict(self):
        out = {}
        for i in range(self.num_aircraft):
            #Generate arrays for initialising the Aircraft objects.
            # pos_array = np.zeros((self.num_t_steps,3))
            # pos_array[0,:] = self.initial_positions[i,:]
            # vel_array = np.zeros((self.num_t_steps,3))
            # vel_array[0,:] = self.initial_velocities[i,:]

            #Call Aircraft class and stores instances in dict
            out[i] = aircraft.Aircraft(i,self.initial_positions[i,:],self.initial_velocities[i,:],self.end_points[i,:])

        return out

    def generate_random_path(self):
        for key,aircraft in self.aircraft_dict.items():
            aircraft.make_random_path(self.delta_t,self.num_t_steps)


    def calc_no_crashes(self):
        #From a random evolution of the initial scenario, work out the total number of crashes that occur(ed)


        #Matrix to store if each pair of aircraft crashed during the evolution
        #should be1 if pair of aircraft crashed, 0 else
        crashed_matrix = np.zeros((self.num_aircraft,self.num_aircraft))

        #Calculate pairwise distance between planes at each timestep.
        for timestep in range(self.num_t_steps):
            #Extract position of each aircraft at timestep
            position_list = np.zeros((self.num_aircraft,3))
            for i in range(self.num_aircraft):
                position_list[i,:] = self.aircraft_dict[i].random_path_position[timestep,:]

            distance_matrix = metrics.calc_pairwise_distance_matrix(position_list)
            crashed_matrix[np.where((distance_matrix<self.separation_threshold) & (distance_matrix>0),1,0).nonzero()]=1
            
        return np.sum(crashed_matrix)
