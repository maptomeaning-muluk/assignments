import arcpy

arcpy.env.workspace = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Practical_One\Practical_One.gdb"

# Specify the feature class you want to buffer
input_feature_class = "Wilson_Schools"
output_feature_class = "Wilson_School_MultiRingBuffer_non_dissolve"
# Specify buffer distances
buffer_distances = [1000, 1200, 1400]

arcpy.analysis.MultipleRingBuffer(input_feature_class,
                                  output_feature_class,
                                  buffer_distances,
                                  "Feet",
                                  "",
                                  "NONE")

print("process completed")

