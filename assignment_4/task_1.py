"""Task 1: Convert any feature class into a feature layer and print the count of features inside the feature layer."""

import arcpy
import os

path_to_gdb = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
crimes_fc_name = "Wilson_Crimes96"
histdist_fc_name = "Wilson_Histdist"

restaurant_fc_path = os.path.join(path_to_gdb, restaurant_fc_name)
crimes_fc_path = os.path.join(path_to_gdb, crimes_fc_name)
histdist_fc_path = os.path.join(path_to_gdb, histdist_fc_name)

features = [restaurant_fc_path, crimes_fc_path, histdist_fc_path]
fc_names = [restaurant_fc_name, crimes_fc_name, histdist_fc_name]

for f,fc in zip(features,fc_names):
    arcpy.management.MakeFeatureLayer(f, "{}_Feature_Layer".format(f))  # iterate to convert into feature layer
    pre_count = arcpy.GetCount_management("{}_Feature_Layer".format(f)) # iterarte to get count from feature layer

    print("The number of {} in wilson are:{}".format(fc, pre_count[0]))
print("process completed")