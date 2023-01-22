import numpy as np
import scenario

def calc_known_risk(Scenario, num_random_paths):
    num_crashed = np.zeros(num_random_paths)
    for i in range(num_random_paths):
        Scenario.generate_random_path()
        num_crashed[i] = Scenario.calc_no_crashes()
    return num_crashed

# def calc_unknown_risk(aircraft_dict):
#     #Placeholder - needs doing
#     unknown_risk = 0
#     return unknown_risk