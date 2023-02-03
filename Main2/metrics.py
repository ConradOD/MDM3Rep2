import numpy as np
import pandas as pd

class Metrics:
    def __init__(self,_Parameters, _Data,_aircraft_a,_aircraft_b):
        #Input data
        self.Parameters = _Parameters
        self.Data = _Data
        self.aircraft_a = _aircraft_a
        self.aircraft_b = _aircraft_b

        self.metric_names = ['distance','yaw_diff','pitch_diff','shortest_dist_timed','shortest_dist_path','dist_f_expected_path']
        self.data_dict = {}

    def data_out(self):
        return pd.Series(self.data_dict).to_frame(1).T

    def calc_all_metrics(self):
        self.metric_calc_distance()
        self.metric_calc_pitch_difference()
        self.metric_calc_yaw_difference()
        self.metric_shortest_distance_timedependent()
        self.metric_shortest_distance_path()
        self.metric_distance_from_expected_path()

    def metric_calc_distance(self):
        #The distance between the two aircraft's current position at each timestep
        self.data_dict['distance'] = np.linalg.norm(self.aircraft_a.position - self.aircraft_b.position)

    def metric_calc_pitch_difference(self):
        #The difference between the two aircraft's current pitch at each timestep
        d_a = self.aircraft_a.velocity
        d_b = self.aircraft_b.velocity
        pitch_a = np.arctan(d_a[2]/(np.sqrt(d_a[0]**2 + d_a[1]**2) ))
        pitch_b = np.arctan(d_b[2]/(np.sqrt(d_b[0]**2 + d_b[1]**2) ))
        self.data_dict['pitch_diff'] = abs(pitch_a - pitch_b)

    def metric_calc_yaw_difference(self):
        #The difference between the two aircraft's current yaw at each timestep
        d_a = self.aircraft_a.velocity
        d_b = self.aircraft_b.velocity
        yaw_a = np.arctan(d_a[1]/(np.sqrt(d_a[0]**2 + d_a[2]**2) ))
        yaw_b = np.arctan(d_b[1]/(np.sqrt(d_b[0]**2 + d_b[2]**2) ))
        self.data_dict['yaw_diff'] = abs(yaw_a - yaw_b)

    def metric_shortest_distance_timedependent(self):
        #The shortest distance between the aircraft on their expected paths, considering their relative motion along the paths.
        #This might change slightly over time, due to the random movement, this is important for short term prediction
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
        #The shortest between the two expected paths, without considering the relative motion of the aircraft.
        #This should remain constant as the paths don't change.
        normal_line = np.cross(self.aircraft_a.direction,self.aircraft_b.direction)
        if np.linalg.norm(normal_line) != 0:
            dist = abs(np.dot(normal_line, self.aircraft_a.start_point-self.aircraft_b.start_point)) / np.linalg.norm(normal_line)
        else:
            cross_product = np.cross(self.aircraft_a.direction, self.aircraft_b.start_point- self.aircraft_a.start_point)
            magnitude_cross = np.linalg.norm(cross_product)
            magnitude_a = np.linalg.norm(self.aircraft_a.direction)
            dist = magnitude_cross/magnitude_a
        self.data_dict['shortest_dist_path'] = dist

    def metric_distance_from_expected_path(self):
        #The distance of the aircraft's current position to its initial expected path. This should change each timestep
        cross_product_a = np.cross(self.aircraft_a.direction, self.aircraft_a.position- self.aircraft_a.start_point)
        magnitude_cross_a = np.linalg.norm(cross_product_a)
        magnitude_a = np.linalg.norm(self.aircraft_a.direction)
        dist_a = np.linalg.norm(magnitude_cross_a/magnitude_a)

        cross_product_b = np.cross(self.aircraft_b.direction, self.aircraft_b.position- self.aircraft_b.start_point)
        magnitude_cross_b = np.linalg.norm(cross_product_b)
        magnitude_b = np.linalg.norm(self.aircraft_b.direction)
        dist_b = np.linalg.norm(magnitude_cross_b/magnitude_b)

        self.data_dict['dist_f_expected_path'] = dist_a + dist_b
