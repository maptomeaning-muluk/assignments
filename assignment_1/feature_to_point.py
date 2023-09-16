import arcpy

arcpy.env.workspace = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Practical_One\Practical_One.gdb"

# Specify the feature class you want to convert
input_feature_class = "Wilson_Zoning"
output_feature_class = "Wilson_Zoning_Point"

arcpy.management.FeatureToPoint(input_feature_class,
                                output_feature_class,
                                "CENTROID")

print("process complete")