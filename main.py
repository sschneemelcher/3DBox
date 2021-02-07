import eel
import numpy as np
import datetime

def rotate(arr, x, y, z):
	cos_z, sin_z, cos_y = np.cos(z), np.sin(z), np.cos(y)
	sin_y, cos_x, sin_x = np.sin(y), np.cos(x), np.sin(x)
	rot_mat = [[cos_z*cos_y, cos_z*sin_y*sin_x - sin_z*cos_x, cos_z*sin_y*cos_x + sin_z*sin_x],
		   [sin_z*cos_y, sin_z*sin_y*sin_x + cos_z*cos_x, sin_z*sin_y*cos_x - cos_z*sin_x],
		   [-sin_y,      cos_y*sin_x,                     cos_y*cos_x                    ]]
	return np.dot(rot_mat, arr).astype(np.float32)

def get_fps(fps, start):
	print(fps)
	return 0, datetime.datetime.now()

def next_step(b, r, f):
	b = rotate(b-offset, r[0]*deg, r[1]*deg, r[2]*deg)+offset
	r = r*0.99 + np.random.normal(0, sigma, 3)*0.01
	f += 1
	eel.sleep(0.0001)
	return b, r, f, []

deg = np.pi/1024
offset = 300
scale = 125
box = np.array([[-1, -1, -1, -1, 1, 1, 1, 1],
		[-1, -1, 1, 1, -1, -1, 1, 1],
		[-1, 1, -1, 1, -1, 1, -1, 1]])*scale+offset
connections = [0,1,0,2,0,4,1,3,1,5,2,3,2,6,3,7,4,5,4,6,5,7,6,7]
sigma = 5
r = np.random.normal(0, sigma, 3)
fps = 0
start = datetime.datetime.now()
coordinates = []

eel.init('app')
eel.start('index.html', size=(620,620), block=False)

while True:
	if (datetime.datetime.now() - start).seconds:
		fps, start = get_fps(fps, start)
	for c in range(len(connections)//2):
		coordinates.append([int(x) for x in list(box[0:2,connections[2*c:2*c+2]].T.flatten())])
	eel.drawLines(coordinates)
	box, r, fps, coordinates = next_step(box, r, fps)
