import numpy as np

class Aircraft:
    
    def __init__(self, _identifier, _position, _velocity, _direction, _acceleration):
        self.id = _identifier
        # Do we want the co - ords in the init ? Or method for the generation?)
        self.position = _position #[x,y,z] initial pos
        self.velocity = _velocity #[x,y,z] intial vel
        self.direction = _direction #[x,y,z]
        self.acceleration = _acceleration

    def get_correction_acceleration(self):
        return np.array([0,0,0])

    def make_random_path(self,_Parameters):
        self.random_path_position = np.zeros((_Parameters.num_t_steps,3))
        self.random_path_velocity = np.zeros((_Parameters.num_t_steps,3))
        self.random_path_acceleration = np.zeros((_Parameters.num_t_steps,3))

        #Set inital coord according to initial pos & vel of aircraft
        self.random_path_position[0,:] = self.position
        self.random_path_velocity[0,:] = self.velocity
        self.random_path_acceleration[0,:] = self.acceleration

        #Iterate through the time steps and solve the dynamics
        for t in range(1,_Parameters.num_t_steps):
            self.random_path_position[t] = self.random_path_position[t-1] + self.random_path_velocity[t-1] * _Parameters.delta_t + np.random.uniform(-1,1,3)*10
            self.random_path_velocity[t] = self.random_path_velocity[t-1] + self.random_path_acceleration[t-1] * _Parameters.delta_t
            self.random_path_acceleration[t] = np.random.uniform(-1,1,3) * _Parameters.acceleration_rand + self.get_correction_acceleration()
        
        #Outputs stored for later

        
    