import numpy as np
import scenario

def calc_known_risk(Scenario, num_random_paths):
    crashed = np.zeros(num_random_paths)
    for i in range(num_random_paths):
        Scenario.generate_random_path()
        crashed[i] = scenario.calc_crashed()

    #Normalise regarding num_planes and grid_size etc.
    known_risk = np.mean(crashed)
    return known_risk


# def calc_unknown_risk(aircraft_dict):
#     #Placeholder - needs doing
#     unknown_risk = 0
#     return unknown_risk