import numpy as np


def generate_scenario(num_planes,grid_size):
    '''
    '''
    initial_positions = np.random.rand(num_planes,3) * grid_size
    initial_velocities = np.random.rand(num_planes,3)
    end_points = np.random.rand(num_planes,3) * grid_size

    return [initial_positions, initial_velocities, end_points]