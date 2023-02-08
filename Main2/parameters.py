class Parameters:
    def __init__(self,num_aircraft=10,grid_size=100000,delta_t=30,max_t=600,num_scenarios=10,separation_thresh_hor=9260,separation_thresh_ver=304,vertical_offset=5000,velocity_mag=243,direction_variation=0.5,acceleration_rand = 0.5,correction_mag=0,t_evo_step_size=60,acceleration_mag=1):
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
        self.acceleration_mag = acceleration_mag