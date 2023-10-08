import arcpy
import os

path = r'D:\SEM_III\Programming_3\assignment_project\ProProject_Practical_Two\RASTER_DATA\erelev'

describe_object = arcpy.Describe(path)

# Band count of raster image
band_number = describe_object.bandcount
print('The number of bands in erelev raster is {}'.format(band_number)

# the format of raster
format_raster = describe_object.format
print('The format of erelev raster is {}'.format(format_raster))

# height and width of image
height_raster = describe_object.height
width_raster = describe_object.width

print('The height of erelev raster data is {} and width is {}.'.format(height_raster,width_raster))

# base name of the raster
base_name = os.path.basename(path)
print(base_name)
