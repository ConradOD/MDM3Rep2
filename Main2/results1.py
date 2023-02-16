import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read pkl files
# LAWRENCE VERSION
'''
single_metric1 = pd.read_pickle('Main2\\single_metric.pkl')
single_metric2 = pd.read_pickle('Main2\\single_metric2.pkl')
all_metric1 = pd.read_pickle('Main2\\all_metric.pkl')
all_metric2 = pd.read_pickle('Main2\\all_metric2.pkl')
'''
# CONRAD'S FILE VERISON
single_metric1 = pd.read_pickle('single_metric.pkl')
single_metric2 = pd.read_pickle('single_metric2.pkl')
all_metric1 = pd.read_pickle('all_metric.pkl')
all_metric2 = pd.read_pickle('all_metric2.pkl')

# print(single_metric1.head())
# print(all_metric1.head())

# Vars to use for unpacking
num_repeats = 25
metric_names = ['distance', 'vel_diff', 'yaw_diff', 'pitch_diff', 'shortest_dist_timed', 'shortest_dist_path',
                'dist_f_expected_path', 'ratio_distance', 'ratio_velocity']
combined_name = ['combined']
column_names = ['repeat'] + metric_names + combined_name

model_names = metric_names + combined_name


# Function for unpacking
def unpack_to_df(single_metrics_df, all_metrics_df, offset):
    df = pd.DataFrame(columns=column_names)
    for repeat in range(num_repeats):
        df_index = repeat + offset
        row = {'repeat': df_index}
        for metric_name in metric_names:
            key_search = metric_name + str(repeat)
            row[metric_name] = single_metrics_df.loc[key_search]
        row['combined'] = all_metrics_df.loc['Combined_' + str(repeat)]
        df = pd.concat([df, pd.Series(row).to_frame(1).T])
    return df


# Call function on each set of data
df1 = unpack_to_df(single_metric1, all_metric1, 0)
df2 = unpack_to_df(single_metric2, all_metric2, 25)

# Combine outputs
all_df = pd.concat([df1, df2])


# print(all_df)

# Turn df into arrays foor f1 & acc
def turn_column_into_2arrays(df, column_name):
    column = df.loc[:, column_name]
    num_rows = column.size
    accuracy_array = np.zeros(num_rows)
    f1_array = np.zeros(num_rows)

    i = 0
    for index, val in column.items():
        f1_array[i] = val[0]
        accuracy_array[i] = val[1]
        i += 1
    return [f1_array, accuracy_array]


[test1, test2] = turn_column_into_2arrays(all_df, 'combined')

bar_names = column_names
bar_names.remove('repeat')

f1_score_dict = {}
acc_score_dict = {}

for name in bar_names:
    [f1, acc] = turn_column_into_2arrays(all_df, name)
    f1_name = name + '_f1'
    acc_name = name + '_acc'
    f1_score_dict[f1_name] = f1
    acc_score_dict[acc_name] = acc


def plot_hist(ax, array, title, xlabel):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Frequency')
    # ax.tight_layout()
    ax = plt.hist(array, bins=10)
    return ax


ax1 = plt.subplot(1, 2, 1)
ax1 = plot_hist(ax1, f1_score_dict['combined_f1'], 'Combined F1', 'F1 score')

ax2 = plt.subplot(1, 2, 2)
ax2 = plot_hist(ax2, acc_score_dict['combined_acc'], 'Combined Acc', 'Accuracy score')

plt.tight_layout(pad=3.0)
plt.savefig('Results\\combined_histogram.pdf')
# plt.show()


'''
#--------------------Plotting Section---------------------------
import matplotlib.pyplot as plt
#Setup 3d plotting
ax = plt.figure().add_subplot(projection='3d')

for key,plane in Scenario.aircraft_dict.items():
    pos = plane.random_path_position
    #For each plane plots line of trajectory
    ax.plot(pos[:,0],pos[:,1],pos[:,2],label="Plane {id}".format(id = plane.id))
    #Dot for start pos
    ax.scatter(pos[0,0],pos[0,1],pos[0,2])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.legend()
plt.show()

'''


# --------------------- VIOLIN PLOT ------------------------


def plot_violin(zero_or_one, data_frame_input, model_names):
    # zero = f1 score , one = accuracy score
    # Data frame is the data to be used in the array extracting functions
    f1_score_dict = {}
    acc_score_dict = {}
    name_order = []
    data_to_plot = []

    for name in model_names:
        [f1, acc] = turn_column_into_2arrays(data_frame_input, name)
        f1_name = name + '_f1'
        acc_name = name + '_acc'
        f1_score_dict[f1_name] = f1
        acc_score_dict[acc_name] = acc

    if zero_or_one == 0:

        for key, value in f1_score_dict.items():
            name_order.append(key)
            data_to_plot.append(value)
        title_label = "Box plot to show the F1 Score Performance of Each Model"


    elif zero_or_one == 1:
        for key, value in acc_score_dict.items():
            name_order.append(key)
            data_to_plot.append(value)
        title_label = "Box plot to show the Accuracy Score Performance of Each Model"

    fig = plt.figure()

    ax = fig.subplots(1, 1)
    bp = ax.boxplot(data_to_plot)
    plt.title(title_label)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], model_names, rotation=30, ha="right")

    fig.tight_layout()
    plt.grid()
    plt.savefig('box_plot' + str(zero_or_one) + '.pdf')
    plt.show()


plot_violin(1, all_df, model_names)


def statistics_df(zero_or_one, data_frame_input, model_names, model_out_index):
    # zero = f1 score , one = accuracy score
    # Data frame is the data to be used in the array extracting functions
    f1_score_dict = {}
    acc_score_dict = {}
    name_order = []
    data_to_plot = []

    for name in model_names:
        [f1, acc] = turn_column_into_2arrays(data_frame_input, name)
        f1_name = name + '_f1'
        acc_name = name + '_acc'
        f1_score_dict[f1_name] = f1
        acc_score_dict[acc_name] = acc

    if zero_or_one == 0:

        for key, value in f1_score_dict.items():
            name_order.append(key)
            data_to_plot.append(value)
        title_label = "Box plot to show the F1 Score Performance of Each Model"


    elif zero_or_one == 1:
        for key, value in acc_score_dict.items():
            name_order.append(key)
            data_to_plot.append(value)
        title_label = "Box plot to show the Accuracy Score Performance of Each Model"

    return data_to_plot[model_out_index]


distance_array = statistics_df(1, all_df, model_names, 1)

mean_combined = np.mean(distance_array)
var_combined = np.var(distance_array)

print(mean_combined, var_combined)
