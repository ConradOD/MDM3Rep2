import numpy as np

class Scenario:
    def __init__(self):
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


    def generate_scenario(num_planes,grid_size):
        '''
        '''
        initial_positions = np.random.rand(num_planes,3) * grid_size
        initial_velocities = np.random.rand(num_planes,3)
        end_points = np.random.rand(num_planes,3) * grid_size

        return [initial_positions, initial_velocities, end_points]