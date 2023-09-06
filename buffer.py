import arcpy

wilson_school_input_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Practical_One\Practical_One.gdb\Wilson_Schools"
wilson_school_buffer_path = r"D:\SEM_III\Programming_3\assignment_project\ProProject_Practical_One\output.gdb\wilson_school_buffer"

#buffer distance
distance = '500 meters'

arcpy.analysis.Buffer(wilson_school_input_path,wilson_school_buffer_path,distance)

print("process completed")