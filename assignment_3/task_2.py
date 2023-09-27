import arcpy
import os

arcpy.env.workspace = r"D:\SEM_III\Programming_3\assignment_project\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

# Output folder path is where the txt file will get created
output_folder_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_AutomatingUsingLists\output_automation"
# Output file name
output_text_file = "MajorAttractions_info.txt"

output_file_path = os.path.join(output_folder_path, output_text_file)

print(output_file_path)

file_obj = open(output_file_path, "w")

# Listing feature class from the gdb
fc_list = arcpy.ListFeatureClasses("MajorAttractions")

for fc_name in fc_list:
    print(fc_name)

print("------------------------------------------------")

# Listing fields and looping fields
field_list = arcpy.ListFields("MajorAttractions")
for field in field_list:
    print("Field Name: {}, Type: {}, Length: {}".format(field.name, field.type, field.length))
    file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))

    print("------------------------------------------")
    file_obj.write("---------------------------------------------\n")
file_obj.close()
print("Process Completed")