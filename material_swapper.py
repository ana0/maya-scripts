import sys

# sys.path.append("~/Applications/Autodesk/maya2016/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages")

# import maya.standalone
# maya.standalone.initialize() 

import maya.cmds as cmds
import math


# def material_swapper(material, piece):
#     cmds.select([piece], replace=True)
#     cmds.sets(e=True, forceElement=material)

def generate_camera_points(angle, radius):
	angles = [math.radians(i) for i in range(360) if i % angle == 0]
	points = [(radius*(math.cos(i)), radius*(math.sin(i)), math.degrees(i)) for i in angles]
	return points

def place_cameras(points):
	for i in points:
		cmds.camera(centerOfInterest=5, focalLength=35, lensSqueezeRatio=1, cameraScale=1, horizontalFilmAperture=1.41732, horizontalFilmOffset=0, 
			verticalFilmAperture=0.94488, verticalFilmOffset=0, filmFit="fill", overscan=1, motionBlur=0, shutterAngle=144, nearClipPlane=0.1,
			farClipPlane=10000, orthographic=0, orthographicWidth=30, panZoomEnabled=0, horizontalPan=0, verticalPan=0, zoom=1)
		cmds.move(i[0], 5.0, i[1])
		#cmds.rotate(0.0, i[2]+90, 0.0, absolute=True, objectSpace=True, forceOrderXYZ=True)
		cmds.viewPlace(lookAt=[0, 0, 0])



# material_swapper("Black", "frontsClassics")

cats = generate_camera_points(6, 17)
place_cameras(cats)
# for i in cats:
# 	print i