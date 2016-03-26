'''main.py
Description: (will run the simulation, increaseing spinning speed until failture)
Args: glass size, amount of water, distance from center, friction
Return: what failed, at what speed
'''

import src.glass_slides as glass_slides
import src.water_shape as water_shape
import src.glass_tips as glass_tips

glass_info = {
	'height': .2,		# m
	'b_radius': .04,	# m
	't_radius': .05,  	# m
	'thickness': .005,  # m
	'density': 2500,  	# kg/m^3
	'c_f': 1,			# unitless
	'percent_full': .5,	# unitless
	'start_radius': .1	# m
}

def run_simulation(glass_info, speed):
	'''Runs the simulation at a given speed, returns what occurs.

	 Args:
	 	glass_info : dictionary of information about glass_info
	 	speed : speed in radians per second

	 Returns:
	 	result: tuple of what occurs 
	 			(glass slides, water reaches brim, glass tips)
	 			0 - nothing happened, 
	 			1 - event occured
	 '''

	 slides = glass_slides.main(glass_info, speed)
	 brim, delta_water_cg = water_shape.main(glass_info, speed)
	 tips = glass_tips.main(glass_info, delta_water_cg, speed)

	 return (slides, brim, tips)


def find_speed(interval=1):
	'''Returns speed at which one of the following occurs:
	1) glass slides off tray
	2) glass tips over
	3) water in glass is flung out of glass
	and which of the three occurs.

	Args:
		interval : step size for increasing speed (rad/s)

	Returns:
		result : tuple of speed, value (1, 2 or 3)
	'''

	speed = 0  # rad/s
	max_speed = 100
	event_occurred = False

	while not event_occurred or speed <= max_speed:
		print "Running simulation at", speed, "rad/s..."
		curr_result = run_simulation(glass_info, speed)
		if sum(curr_result) == 1:
			event_occurred = True
		elif sum(curr_result) > 1:
			raise ValueError('More than one event occurred! Try decreasing your interval.')
		speed += interval

	if event_occurred:
		return (speed, curr_result.index(1)+1)
	else:
		raise ValueError('No event occurred. Something went wrong?')

if __name__ == "__main__":
	print find_speed()