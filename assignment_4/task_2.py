#Task 2: Print the crime count within 500 meters distance from all the restaurants.
import arcpy
import os
gdb_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Selections\ProProject_Selections.gdb"

restaurant_fc_name = "Wilson_Restaurants"
crimes_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
crimes_fc_path = os.path.join(gdb_path,crimes_fc_name)
# converting feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_layer")
arcpy.management.MakeFeatureLayer(crimes_fc_path, "crimes_layer")

arcpy.management.SelectLayerByLocation("crimes_layer", "WITHIN_A_DISTANCE", "restaurant_layer", "500 meters")
post_count = arcpy.GetCount_management("crimes_layer")
print("The number of crimes within 500 meters from restaurants in Wilson: {}".format(post_count[0]))

