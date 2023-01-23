class Parameters:
    def __init__(self,num_aircraft=5,grid_size=100,delta_t=0.5,max_t=10,num_scenarios=50,separation_thresh_hor=5,separation_thresh_ver=5):
        self.num_aircraft = num_aircraft
        self.grid_size = grid_size
        self.delta_t = delta_t
        self.max_t = max_t
        self.num_t_steps = int(self.max_t / self.delta_t)
        self.num_scenarios = num_scenarios
        self.num_pairs = int( self.num_aircraft*(self.num_aircraft-1)/2)
        self.separation_thresh_hor = separation_thresh_hor
        self.separation_thresh_ver = separation_thresh_ver