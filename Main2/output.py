import numpy as np

class Output:
    def __init__(self,_Parameters,_Scenario):
        self.Parameters = _Parameters
        self.Scenario = _Scenario
        self.output_name = ['crashed']

    def make_crashed_dict(self):
        self.crashed_dict = {}
        for id,pair in self.Scenario.aircraft_pair_dict.items():
            crashed = self.calc_if_pair_crashes(pair)
            self.crashed_dict[id] = crashed

    def calc_if_pair_crashes(self,pair):
        aircraft_a = self.Scenario.aircraft_dict[pair[0]]
        aircraft_b = self.Scenario.aircraft_dict[pair[1]]

        crashed = 0
        for timestep in range(self.Parameters.num_t_steps):
            pos_a = aircraft_a.random_path_position[timestep,:]
            pos_b = aircraft_b.random_path_position[timestep,:]

            horizontal_dist = np.linalg.norm(pos_a[0:1] - pos_b[0:1])
            vertical_dist = np.linalg.norm(pos_a[2] - pos_b[2])

            if horizontal_dist <= self.Parameters.separation_thresh_hor or vertical_dist <= self.Parameters.separation_thresh_ver:
                crashed = 1

        return crashed