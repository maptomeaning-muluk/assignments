import arcpy
import os

path = r'D:\SEM_III\Programming_3\assignment_project\ProProject_Practical_Two\World_data.gdb\Lakes'

describe_object = arcpy.Describe(path)

# spatial reference of the feature class lakes
"""spatial_reference = describe_object.spatialReference
print(spatial_reference.name)
print(spatial_reference.type)"""

# describe feature type
'''feature_type = describe_object.datasetType
print("The type of feature class Lakes is:{}".format(feature_type))'''

# describe every field in the and field type
field_list = describe_object.fields
for f in field_list:
    field_name = f.name
    field_type = f.type

    print("In Lakes have field name: {} which field type is {}".format(field_name,field_type))
