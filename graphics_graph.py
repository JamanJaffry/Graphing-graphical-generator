def calc_linear_points(start, stop, interval, m, c):
	# This function returns a list of points from start to stop with a gap of interval for the equation y = mx + c
	points = []
	x = float(start)
	while True:
		y = m*x + c
		points.append(y)
		x += interval
		if x > stop:
			break
	return points

print(calc_linear_points(5, 10, 0.5, 2, 3))
