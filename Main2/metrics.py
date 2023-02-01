import numpy as np
import pandas as pd

class Metrics:
    def __init__(self,_Parameters,_aircraft_a,_aircraft_b):
        #Input data
        self.Parameters = _Parameters
        self.aircraft_a = _aircraft_a
        self.aircraft_b = _aircraft_b

        self.metric_names = ['distance','yaw_diff','pitch_diff','shortest_dist_timed','shortest_dist_path']
        self.data_dict = {}

    def data_out(self):
        return pd.Series(self.data_dict).to_frame(1).T

    def calc_all_metrics(self):
        self.metric_calc_distance()
        self.metric_calc_pitch_difference()
        self.metric_calc_yaw_difference()
        self.metric_shortest_distance_timedependent()
        self.metric_shortest_distance_path()

    def metric_calc_distance(self):
        self.data_dict['distance'] = np.linalg.norm(self.aircraft_a.position - self.aircraft_b.position)

    def metric_calc_pitch_difference(self):
        d_a = self.aircraft_a.direction
        d_b = self.aircraft_b.direction
        pitch_a = np.arctan(d_a[2]/(np.sqrt(d_a[0]**2 + d_a[1]**2) ))
        pitch_b = np.arctan(d_b[2]/(np.sqrt(d_b[0]**2 + d_b[1]**2) ))
        self.data_dict['pitch_diff'] = abs(pitch_a - pitch_b)

    def metric_calc_yaw_difference(self):
        d_a = self.aircraft_a.direction
        d_b = self.aircraft_b.direction
        yaw_a = np.arctan(d_a[1]/(np.sqrt(d_a[0]**2 + d_a[2]**2) ))
        yaw_b = np.arctan(d_b[1]/(np.sqrt(d_b[0]**2 + d_b[2]**2) ))
        self.data_dict['yaw_diff'] = abs(yaw_a - yaw_b)

    def metric_shortest_distance_timedependent(self):
        pos_a = np.zeros((self.Parameters.num_t_steps,3))
        pos_b = np.zeros((self.Parameters.num_t_steps,3))
        pos_a[0,:] = self.aircraft_a.position
        pos_b[0,:] = self.aircraft_b.position
        for timestep in range(self.Parameters.num_t_steps-1):
            pos_a[timestep+1,:] = pos_a[timestep,:] + self.aircraft_a.direction * self.Parameters.delta_t
            pos_b[timestep+1,:] = pos_b[timestep,:] + self.aircraft_b.direction * self.Parameters.delta_t

        dist_between = np.linalg.norm(pos_a - pos_b, axis=1)
        self.data_dict['shortest_dist_timed'] = dist_between.min()

    def metric_shortest_distance_path(self):
        normal_line = np.cross(self.aircraft_a.direction,self.aircraft_b.direction)
        if normal_line != 0:
            dist = abs(np.dot(normal_line, self.aircraft_a.position-self.aircraft_b.position)) / np.linalg.norm(normal_line)
        else:
            dist = 0
        self.data_dict['shortest_dist_path'] = dist

