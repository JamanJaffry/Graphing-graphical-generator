import pygame, sys
from pygame.locals import *

def calc_linear_points(start, stop, interval, m, c):
	# This function returns a list of points from start to stop with a gap of interval for the equation y = mx + c
	points = []
	x = float(start)
	while True:
		y = m*x + c
		points.append([x, y])
		x += interval
		if x > stop:
			break
	return points

def calc_quadratic_points(start, stop, interval, a, b, c):
	# This function returns a list of points from start to stop with a gap of interval for the equation y = ax^2 + bx + c
	points = []
	x = float(start)
	while True:
		y = a*(x**2) + b*x + c
		points.append([x, y])
		x += interval
		if x > stop:
			break
	return points

def draw_points(array_of_points, point_size, scale_x, scale_y, offset_x, offset_y):
	# This function makes a new window showing the points.
	print("window opened")
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((400, 300))
	pygame.display.set_caption("Graphing window")
		
	DISPLAYSURF.fill((255, 255, 255)) # Make a white background
	for i in array_of_points:
		pygame.draw.circle(DISPLAYSURF, (255, 0, 0), (int(i[0])*scale_x + offset_x, int(i[1])*scale_y + offset_y), point_size, 0) # Draw a small circle at every point
			
	running = True
	while True: # Main pygame loop
		pygame.display.update() # Update the window
		for event in pygame.event.get(): # Checks if the user presses the close button
			if event.type == QUIT:
				pygame.quit()
				running = False
		if running == False:
			break
	print("window closed")

points_a = calc_linear_points(5, 10, 0.5, 2, 3)
points_b = calc_quadratic_points(-7, 20, 2, 2, -4, 8)

print(points_a)
print(points_b)

draw_points(points_a, 10, 10, 1, 0, 0)
draw_points(points_b, 10, 10, 1, 100, 0)
