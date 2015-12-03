import sys

# sys.path.append("~/Applications/Autodesk/maya2016/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages")

# import maya.standalone
# maya.standalone.initialize() 

# import maya.cmds as cmds

import math


# def material_swapper(material, piece):
#     cmds.select([piece], replace=True)
#     cmds.sets(e=True, forceElement=material)

def generate_camera_points(angle, radius):
	angles = [math.radians(i) for i in range(360) if i % angle == 0]
	points = [(radius*(math.cos(i)), radius*(math.sin(i))) for i in angles]
	return points


# material_swapper("Black", "frontsClassics")

print generate_camera_points(6, 17)