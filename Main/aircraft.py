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

class Aircraft:
    
    def __init__(self, _identifier, _position, _velocity, _end_point):
        self.id = _identifier
        # Do we want the co - ords in the init ? Or method for the generation?)
        self.position = _position #[x,y,z] (n,3) shape, n timesteps
        self.velocity = _velocity
        self.end_point = _end_point
        

    def generate_known_path(self,max_t,delta_t):
        num_t_steps = int(max_t / delta_t)
        for t in range(num_t_steps-1):
            self.position[t] = self.position[t-1] + self.velocity[t-1] * delta_t


    def route_gen_method(self,):
        pass
    
    def update_position(self,delta_t):
        pass
        #self.position[t,:] = self.position[t-1] + self.velocity[t-1] * delta_t

        
    