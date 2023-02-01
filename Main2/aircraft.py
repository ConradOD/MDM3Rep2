import numpy as np

class Aircraft:
    
    def __init__(self, _Parameters, _identifier, _position, _velocity, _direction, _acceleration):
        self.Parameters = _Parameters
        self.id = _identifier
        # Do we want the co - ords in the init ? Or method for the generation?)
        self.position = _position #[x,y,z] initial pos
        self.velocity = _velocity #[x,y,z] intial vel
        self.direction = _direction #[x,y,z]
        self.acceleration = _acceleration

    def get_correction_acceleration(self, current_position):
        #point = np.array(point)
        point = current_position
        #line_point = np.array(line_point)
        line_point = self.position

        #line_direction = np.array(line_direction)
        line_direction = self.direction

        shortest_direction = np.cross(point - (line_point + np.dot((point - line_point), line_direction) * line_direction), line_direction)
        if np.linalg.norm(shortest_direction) == 0:
            return shortest_direction
        else:
            return shortest_direction / np.linalg.norm(shortest_direction) * self.Parameters.correction_mag

    def make_random_path(self):
        self.random_path_position = np.zeros((self.Parameters.num_t_steps,3))
        self.random_path_velocity = np.zeros((self.Parameters.num_t_steps,3))
        self.random_path_acceleration = np.zeros((self.Parameters.num_t_steps,3))

        #Set inital coord according to initial pos & vel of aircraft
        self.random_path_position[0,:] = self.position
        self.random_path_velocity[0,:] = self.velocity
        self.random_path_acceleration[0,:] = self.acceleration

        #Iterate through the time steps and solve the dynamics
        for t in range(1,self.Parameters.num_t_steps):
            self.random_path_position[t,:] = self.random_path_position[t-1,:] + self.random_path_velocity[t-1,:] * self.Parameters.delta_t + np.random.uniform(-1,1,3)*10
            self.random_path_velocity[t,:] = self.random_path_velocity[t-1,:] + self.random_path_acceleration[t-1,:] * self.Parameters.delta_t
            self.random_path_acceleration[t,:] = np.random.uniform(-1,1,3) * self.Parameters.acceleration_rand + self.get_correction_acceleration(self.random_path_position[t-1])

    def move_along_path(self,timestep):
        #Set attributes of aircraft according to random path at timestep
        self.position = self.random_path_position[timestep,:]
        self.velocity = self.random_path_velocity[timestep,:] 
        self.acceleration = self.random_path_acceleration[timestep,:]
        
    