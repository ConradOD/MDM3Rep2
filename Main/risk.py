import scenario

def calc_known_risk(Scenario, num_random_paths):
    crashed = []
    for i in range(num_random_paths):
        Scenario.make_path()
        crashed[i] = scenario.calc_crashed()

    #Normalise regarding num_planes and grid_size etc.
    known_risk = mean(crashed)
    return known_risk


def calc_unknown_risk(aircraft_dict):
    #Placeholder - needs doing
    unknown_risk = 0
    return unknown_risk