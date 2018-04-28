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

def draw_points(array_of_points, point_size):
	# This function makes a new window showing the points.
	print("window opened")
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Graphing window")
	
	offset_x = 0
	offset_y = 0

	scale_x = 1
	scale_y = 1

	running = True

	while True: # Main pygame loop
		DISPLAYSURF.fill(WHITE) # Make a white background

#		Glitchy scrolling axes code FIX LATER
#		pygame.draw.line(DISPLAYSURF, BLUE, (-999, (height//2 + offset_y) // scale_y), (999, (height//2 + offset_y) // scale_y), 4) # Draw the x and y axes
#		pygame.draw.line(DISPLAYSURF, GREEN, ((width//2 + offset_x) // scale_x, -999), ((width//2 + offset_x) // scale_x, 999), 4)

		pygame.draw.line(DISPLAYSURF, BLUE, (-999, height//2 + offset_y), (999, height//2 + offset_y), 4) # Draw the x and y axes
		pygame.draw.line(DISPLAYSURF, GREEN, (width//2 + offset_x, -999), (width//2 + offset_x, 999), 4)

		for i in array_of_points:# Draw the points
			pygame.draw.circle(DISPLAYSURF, RED, (int(i[0]*scale_x + offset_x), int(i[1]*scale_y + offset_y)), point_size, 0) # Draw a small circle at every point


		keys = pygame.key.get_pressed() # Check for keypress for scrolling the window
		# Keys for scroll
		if keys[K_LEFT]: offset_x += x_speed
		if keys[K_RIGHT]: offset_x -= x_speed
		if keys[K_UP]: offset_y += y_speed
		if keys[K_DOWN]: offset_y -= y_speed
		# Keys for zooming
		if keys[K_w]: scale_x += x_scale_speed; scale_y += y_scale_speed 
		if keys[K_s]: scale_x -= x_scale_speed; scale_y -= y_scale_speed
		
		pygame.display.update() # Update the window
		clock.tick(FPS)

		for event in pygame.event.get(): # Checks if the user presses the close button
			if event.type == QUIT:
				pygame.quit()
				running = False
		if running == False:
			break
	print("window closed")

clock = pygame.time.Clock()

# Constants for colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

# Framerate
FPS = 30

# Speed of scrolling
x_speed = 60/FPS
y_speed = 60/FPS

x_scale_speed = 60/FPS
y_scale_speed = 60/FPS


# Window dimentions
width = 400
height = 300

points_a = calc_linear_points(5, 10, 0.5, 2, 3)
points_b = calc_quadratic_points(-7, 20, 2, 2, -4, 8)

print(points_a)
print(points_b)

draw_points(points_a, 10)
draw_points(points_b, 10)
