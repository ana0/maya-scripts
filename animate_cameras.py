import maya.cmds as cmds
import math
import datetime


def generate_camera_points(angle, radius):
	angles = [math.radians(i) for i in range(360) if i % angle == 0]
	points = [(radius*(math.cos(i)), radius*(math.sin(i))) for i in angles]
	return points

# def place_cameras(points):
# 	"""create a ring of cameras in a circle around main object, pointing at it"""
# 	for i in points:
# 		cmds.camera(centerOfInterest=5, focalLength=35, lensSqueezeRatio=1, cameraScale=1, horizontalFilmAperture=1.41732, horizontalFilmOffset=0, 
# 			verticalFilmAperture=0.94488, verticalFilmOffset=0, filmFit="fill", overscan=1, motionBlur=0, shutterAngle=144, nearClipPlane=0.1,
# 			farClipPlane=10000, orthographic=0, orthographicWidth=30, panZoomEnabled=0, horizontalPan=0, verticalPan=0, zoom=1)
# 		cmds.move(i[0], 5.0, i[1])
# 		cmds.viewPlace(lookAt=[0, 3.0, 0])

def camera_init(points):
	"""initiate camera at first point"""
	camera = cmds.camera(centerOfInterest=5, focalLength=35, lensSqueezeRatio=1, cameraScale=1, horizontalFilmAperture=1.41732, horizontalFilmOffset=0, 
	verticalFilmAperture=0.94488, verticalFilmOffset=0, filmFit="fill", overscan=1, motionBlur=0, shutterAngle=144, nearClipPlane=0.1,
	farClipPlane=10000, orthographic=0, orthographicWidth=30, panZoomEnabled=0, horizontalPan=0, verticalPan=0, zoom=1)
	cmds.move(points[0][0], 5.0, points[0][1])
	cmds.viewPlace(lookAt=[0, 3.0, 0])
	return camera

def camera_anim(points, camera):
	# cameras = cmds.listCameras(perspective=True)
	cmds.select([camera], replace=True)
	for i in points:
	# cmds.camera(centerOfInterest=5, focalLength=35, lensSqueezeRatio=1, cameraScale=1, horizontalFilmAperture=1.41732, horizontalFilmOffset=0, 
	# 	verticalFilmAperture=0.94488, verticalFilmOffset=0, filmFit="fill", overscan=1, motionBlur=0, shutterAngle=144, nearClipPlane=0.1,
	# 	farClipPlane=10000, orthographic=0, orthographicWidth=30, panZoomEnabled=0, horizontalPan=0, verticalPan=0, zoom=1)
		cmds.currentTime(i+1)
		# cmds.select([camera], replace=True)
		cmds.move(i[0], 5.0, i[1])
		cmds.viewPlace(lookAt=[0, 3.0, 0])
		cmds.setKeyframe()

cats = generate_camera_points(6, 23)
camera_main = camera_init(cats)
camera_anim(cats, camera_main)