# Bringing a Gun to a Guard Fight
# ===============================

# Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, 
# you grabbed a beam weapon from an abandoned guardpost while you were running through the station,
# so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well
# as to the elite guard: its beams reflect off walls, meaning you'll have to be very careful where you shoot
# to avoid bouncing a shot toward yourself!

# Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage.
# You also know that if a beam hits a corner, it will bounce back in exactly the same direction. 
# And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully). 

# Write a function answer(dimensions, your_position, guard_position, distance) that gives an array of
# 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room,
# an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions 
# that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

# The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both
# positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. 
# Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

# For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], 
# guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the 
# elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], 
# and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int list) dimensions = [3, 2]
#     (int list) your_position = [1, 1]
#     (int list) guard_position = [2, 1]
#     (int) distance = 4
# Output:
#     (int) 7

# Inputs:
#     (int list) dimensions = [300, 275]
#     (int list) your_position = [150, 150]
#     (int list) guard_position = [185, 100]
#     (int) distance = 500
# Output:
#     (int) 9

# Use verify [file] to test your solution and see how it does. 
# When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.

import math

def answer(dimensions, your_position, guard_position, distance):
	grid = []


	# The top two for loops build the grid
	#	The top for loop "Row Loop" - loops for number of rows of rooms
	#	The second for loop "Col Loop" - loops for number of Columnds of rooms

	# row loop
	for x in range(-(distance//dimensions[1])-1, (distance//dimensions[1])+2):
		# print("### IN ROW LOOP ###")
		x_coords = [0,0]
		g_coords = [0,0]
		
		# print("Dimensions: ", dimensions[1])
		# print("Your Posit: ", your_position[1])
		# print("Difference: ", dimensions[1] - your_position[1])

		# If the row number is even:
		# 	Your y position will be the same as the original
		# else:
		# 	Your y position is flipped over the vertical axis
		if x % 2 == 0:
			x_coords[1] = your_position[1]
			g_coords[1] = guard_position[1]
			# print("x_coords = your_position: ",your_position[1])
		else:
			x_coords[1] = dimensions[1] - your_position[1]
			g_coords[1] = dimensions[1] - guard_position[1]
			# print("x_coords = Difference   : ", dimensions[1] - your_position[1])
		
		row = []
		# column loop
		for i in range(-(distance//dimensions[0])-1, (distance//dimensions[0])+2):
			# print("### IN COLUMN LOOP ###")
			final_x = [0,0]
			final_g = [0,0]
			# print("Dimensions: ", dimensions[0])
			# print("Your Posit: ", your_position[0])
			# print("Difference: ", dimensions[0] - your_position[0])
			
			# If the col number is even:
			# 	Your x position will be the same as the original
			# else:
			# 	Your x position is flipped over the horizontal axis
			if i % 2 == 0:
				# pass
				x_coords[0] = your_position[0]
				g_coords[0] = guard_position[0]
				# print("x_coords = your_position: ",your_position[0])
			else:
				# pass
				x_coords[0] = dimensions[0] - your_position[0]
				g_coords[0] = dimensions[0] - guard_position[0]
				# print("x_coords = Difference   : ", dimensions[0] - your_position[0])

			# Adjusting each room from coordinates in each room
			#	to coordinates as a single coordinate plane

			# print("Prior to Adjusting:")
			# print("At Room:")
			# print("x: ", x, "   i: ",i)
			# print("X: ", x_coords)
			# print("G: ", g_coords)
			# print("-"*20)

			# Adjust to relative to inside its own room
			final_x[0] = x_coords[0] - your_position[0]
			final_x[1] = x_coords[1] - your_position[1]
			final_g[0] = g_coords[0] - your_position[0]
			final_g[1] = g_coords[1] - your_position[1]

			# print("After Adjusting within Box:")
			# print("X: ", x_coords)
			# print("G: ", g_coords)
			# print("-"*20)

			# Adjust from relative to inside box to relative to [0,0]
			final_x[0] += ((dimensions[0]) * i) # changes col value
			final_x[1] += ((dimensions[1]) * x) # changes row value
			
			final_g[0] += ((dimensions[0]) * i) # changes col value
			final_g[1] += ((dimensions[1]) * x) # changes row value

			# print("Dimensions: ", dimensions)
			# print("Dimensions[0]+1 * i = ", (dimensions[0]) * i)
			# print("Dimensions[1]+1 * x = ", (dimensions[1]) * x)

			# print("After Adjusting:")
			# print("X: ", final_x)
			# print("G: ", final_g)
			# print("="*20)
			# print("="*20)

			row.append([final_x,final_g])
		grid.append(row)



	grid_length = len(grid)//2
	gridI_length = len(grid[0])//2
	visited = {}
	count  = 0

	# Loop from near [0,0]->distance, row by row, for each "Quadrant"
	# 	Quadrants:
	# 	4 | 1
	# 	-----
	# 	3 | 2
	# 
	# Test for your position first then for Guard position and save all
	#	ArcTan2 values to a dictionary

	# Quadrant 1
	# loop over each row
	for i in range(grid_length,len(grid)):
		# loop over each X & T pair in row
		for j in range(gridI_length,len(grid[i])):
			your_pos = grid[i][j][0]
			guard_pos = grid[i][j][1]
			
			# print(guard_pos, "distance = ", math.hypot(guard_pos[0],guard_pos[1]))
			if distance - math.hypot(guard_pos[0],guard_pos[1]) >= 0:
				x_atan = format(math.atan2(your_pos[1], your_pos[0]),'.32f')
				if your_pos != [0,0]:
					# print("X Value",x_atan, "--",your_pos)
					visited[x_atan] = True
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				# print("G Value",k, "--",guard_pos)
				if k not in visited:
					# print("++K not here")
					count += 1
					visited[k] = True
				# else:
				# 	print ("--",guard_pos[1], guard_pos[0], "is there" , k)
				# print()
			else:
				#pass
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				visited[k] = True

	# Quadrant 4
	# loop over each row
	for i in range(grid_length,len(grid)):
		# loop over each X & T pair in row
		for j in range(gridI_length,-1,-1):
			your_pos = grid[i][j][0]
			guard_pos = grid[i][j][1]
			
			# print(guard_pos, "distance = ", math.hypot(guard_pos[0],guard_pos[1]))
			if distance - math.hypot(guard_pos[0],guard_pos[1]) >= 0:
				x_atan = format(math.atan2(your_pos[1], your_pos[0]),'.32f')
				if your_pos != [0,0]:
					# print("X Value",x_atan, "--",your_pos)
					visited[x_atan] = True
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				# print("G Value",k, "--",guard_pos)
				if k not in visited:
					# print("++K not here")
					count += 1
					visited[k] = True
				# else:
				# 	print ("--",guard_pos[1], guard_pos[0], "is there" , k)
				# print()
			else:
				#pass
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				visited[k] = True


	# Quadrant 2
	# loop over each row
	for i in range(grid_length-1,-1,-1):
		# loop over each X & T pair in row
		for j in range(gridI_length,len(grid[i])):
			your_pos = grid[i][j][0]
			guard_pos = grid[i][j][1]
			
			# print(guard_pos, "distance = ", math.hypot(guard_pos[0],guard_pos[1]))
			if distance - math.hypot(guard_pos[0],guard_pos[1]) >= 0:
				x_atan = format(math.atan2(your_pos[1], your_pos[0]),'.32f')
				if your_pos != [0,0]:
					# print("X Value",x_atan, "--",your_pos)
					visited[x_atan] = True
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				# print("G Value",k, "--",guard_pos)
				if k not in visited:
					# print("++K not here")
					count += 1
					visited[k] = True
				# else:
				# 	print ("--",guard_pos[1], guard_pos[0], "is there" , k)
				# print()
			else:
				#pass
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				visited[k] = True

	# Quadrant 3
	# loop over each row
	for i in range(grid_length-1,-1,-1):
		# loop over each X & T pair in row
		for j in range(gridI_length,-1,-1):
			your_pos = grid[i][j][0]
			guard_pos = grid[i][j][1]
			
			# print(guard_pos, "distance = ", math.hypot(guard_pos[0],guard_pos[1]))
			if distance - math.hypot(guard_pos[0],guard_pos[1]) >= 0:
				x_atan = format(math.atan2(your_pos[1], your_pos[0]),'.32f')
				if your_pos != [0,0]:
					# print("X Value",x_atan, "--",your_pos)
					visited[x_atan] = True
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				# print("G Value",k, "--",guard_pos)
				if k not in visited:
					# print("++K not here")
					count += 1
					visited[k] = True
				# else:
				# 	print ("--",guard_pos[1], guard_pos[0], "is there" , k)
				# print()
			else:
				#pass
				k = format(math.atan2(guard_pos[1], guard_pos[0]),'.32f')
				visited[k] = True


	print (count)
	return count



# Inputs:
# print("Solution 10:")
dimensions =  [4, 10]
your_position =  [1, 5]
guard_position =  [3, 1]
distance = 15
answer(dimensions, your_position, guard_position, distance)
# Output:
#     (int) 17


# Inputs:
dimensions = [3, 2]
your_position = [1, 1]
guard_position = [2, 1]
distance = 4
answer(dimensions, your_position, guard_position, distance)
# Output:
#     (int) 7

# Inputs:
dimensions = [300, 275]
your_position = [150, 150]
guard_position = [185, 100]
distance = 500
answer(dimensions, your_position, guard_position, distance)
# Output:
   # (int) 9

# Inputs:
dimensions = [2, 5]
your_position = [1, 2]
guard_position = [1, 4]
distance = 11
answer(dimensions, your_position, guard_position, distance)
# Output:
#     (int) 27

# Inputs:
# print("Solution 10:")
dimensions = [5, 4]
your_position = [2, 1]
guard_position = [3, 3]
distance = 15
answer(dimensions, your_position, guard_position, distance)
# Output:
#     (int) 34

# Inputs:
dimensions = [42, 59]
your_position = [34, 44]
guard_position = [6, 34]
distance = 5000
answer(dimensions, your_position, guard_position, distance)
# Output:
    # (int) 30904

# Inputs:
dimensions = [23, 10]
your_position = [6, 4]
guard_position = [3, 2]
distance = 23
answer(dimensions, your_position, guard_position, distance)
# Output:
#     (int) 8

# Inputs:
dimensions = [10,10]
captain_position = [4, 4]
badguy_position = [3,3]
distance = 5000
answer(dimensions, your_position, guard_position, distance)
# Output:
#     (int) 739425