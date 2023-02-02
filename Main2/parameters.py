class Parameters:
    def __init__(self,num_aircraft=10,grid_size=1000,delta_t=0.5,max_t=10,num_scenarios=10,separation_thresh_hor=5,separation_thresh_ver=5,vertical_offset=1000,velocity_mag=10,direction_variation=5,acceleration_rand = 1,correction_mag=1,t_evo_step_size=5):
        self.num_aircraft = num_aircraft
        self.grid_size = grid_size
        self.delta_t = delta_t
        self.max_t = max_t
        self.num_t_steps = int(self.max_t / self.delta_t)
        self.num_scenarios = num_scenarios
        self.num_pairs = int( self.num_aircraft*(self.num_aircraft-1)/2)
        self.separation_thresh_hor = separation_thresh_hor
        self.separation_thresh_ver = separation_thresh_ver
        self.vertical_offset = vertical_offset
        self.velocity_mag = velocity_mag
        self.direction_variation = direction_variation
        self.acceleration_rand = acceleration_rand
        self.correction_mag = correction_mag
        self.t_evo_step_size = t_evo_step_size