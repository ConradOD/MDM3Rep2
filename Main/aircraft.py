#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

File containing the aircraft class.

This class, as descirbed by the mindmap has the following properties and methods.


Properties / Attributes;

Dynamics:
    Current t position
    Approx Velocity, Accelation
    


Created on Sun Jan 15 17:42:12 2023

@author: conradodriscoll
"""

import numpy as np

class Aircraft:
    
    def __init__(self, _identifier, _position, _velocity, _end_point):
        self.id = _identifier
        # Do we want the co - ords in the init ? Or method for the generation?)
        self.position = _position #[x,y,z] initial pos
        self.velocity = _velocity #[x,y,z] intial vel
        self.end_point = _end_point #[x,y,z]

    def make_random_path(self,delta_t,num_t_steps):
        self.random_path_position = np.zeros((num_t_steps,3))
        self.random_path_velocity = np.zeros((num_t_steps,3))

        #Set inital coord according to initial pos & vel of aircraft
        self.random_path_position[0,:] = self.position
        self.random_path_velocity[0,:] = self.velocity

        #Iterate through the time steps and solve the dynamics
        for t in range(1,num_t_steps):
            self.random_path_position[t] = self.random_path_position[t-1] + self.random_path_velocity[t-1] * delta_t + np.random.uniform(-1,1,3)*10
            self.random_path_velocity[t] = self.random_path_velocity[t-1]
        
        #Outputs stored for later

        
    