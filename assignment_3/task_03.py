import arcpy

arcpy.env.workspace = r"D:\SEM_III\Programming_3\assignment_project\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

feature_class_list = arcpy.ListFeatureClasses()
print(feature_class_list)

for fc in feature_class_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType


    # add buffer point: 500 ft, polyline: 1000 ft, polygon: 600 ft

    if shape_type == "Point":
        buffer_distance = "300 feet"
    elif shape_type == "Polyline":
        buffer_distance = "2000 feet"
    elif shape_type == "Polygon":
        buffer_distance = "500 feet"

    Output_buffer = fc + "_Buffer"
    arcpy.analysis.Buffer(fc, Output_buffer, buffer_distance)

    print("The shapetype of {} is {}".format(fc,shape_type))


print("process complete")