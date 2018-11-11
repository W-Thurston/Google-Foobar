# Don't Get Volunteered!
# ======================

# As a henchman on Commander Lambda's space station, you're expected to be resourceful, 
# smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies 
# at the same time, after all! In order to make sure that everyone working for her is 
# sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman 
# dormitories. It looks like a chessboard, and every morning and evening you have to solve a 
# new movement puzzle in order to cross the floor. That would be fine if you got to be the rook 
# or the queen, but instead, you have to be the knight. Worse, if you take too much time solving 
# the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

# To help yourself get to and from your bunk every day, write a function called answer(src, dest) 
# which takes in two parameters: the source square, on which you start, and the destination square, 
# which is where you need to land to solve the puzzle.  The function should return an integer 
# representing the smallest number of moves it will take for you to travel from the source square 
# to the destination square using a chess knight's moves (that is, two squares in any direction 
# immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  
# Both the source and destination squares will be an integer between 0 and 63, inclusive, and are 
# numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) src = 19
#     (int) dest = 36
# Output:
#     (int) 1

# Inputs:
#     (int) src = 0
#     (int) dest = 1
# Output:
#     (int) 3

# Use verify [file] to test your solution and see how it does. 
# When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.



src = 0
dst = 0

def answer(src, dst):

	#### Create Grid ####
	grid = []
	for i in range(0,8):
		grid.append([x for x in range(0,8)])
	####

	#### Change numbers to coordinates ####
	src_coords = (src//8,src%8)
	dst_coords = (dst//8,dst%8)
	# print("Src: ", src_coords)
	# print("Dst: ", dst_coords)
	####

	#### Create dictionary holders ####
	master_dict_holder = {}    # All past values, so we don't recompute
	master_dict_test_new = {}  # Temporary holder while looping over old
	master_dict_test_old = {}  # Loop over this dictionary's values for coords

	
	def all_moves(src):
		########
		#  This function calculates all possible "moves" from given coordinate
		# 	Returns a dictionary:
		# 				dict(input: [(posssible_move),(posssible_move),...])
		########

		# Testing location of code
		# print("INSIDE all_moves, src: ", src)


		all_possible_moves = {}

		# Check for () aka empty tuple and then calculate all 8 moves for knight
		if len(src) != 0:
			up_left    = [src[0]-2, src[1]-1]
			up_right   = [src[0]-2, src[1]+1]
			right_up   = [src[0]-1, src[1]+2]
			right_down = [src[0]+1, src[1]+2]
			down_right = [src[0]+2, src[1]+1]
			down_left  = [src[0]+2, src[1]-1]
			left_down  = [src[0]+1, src[1]-2]
			left_up    = [src[0]-1, src[1]-2]

			# Add 8 moves to list
			temp_moves = [up_left, up_right, right_up, right_down,
						  down_right, down_left, left_down, left_up]

			# if any of the moves are outside the grid, replace w/ empty tuple
			#   else change list individual value from list to tuple
			for i in range(len(temp_moves)):
				if ((temp_moves[i][0] not in range(8)) or (temp_moves[i][1] not in range(8))):
					temp_moves[i] = ()
				else:
					temp_moves[i] = tuple(temp_moves[i])

			# Create dict to be returned
			all_possible_moves[src] = temp_moves
			return(all_possible_moves)

		else:
			return (tuple())

	# Intiate Looping dictionary
	master_dict_test_old  = all_moves(src_coords)
	# print("First Moves: ", master_dict_test_old)
	

	def search_for_match(lis):
		########
		#  This function searches a given list for destination coordinates
		# 		The list is going to be the values of a dictionary
		# 	Returns a True/False:
		# 				True if Destination found, else False
		########
		for v in lis:
			# print(v)
			if v == dst_coords:
				# print("FOUND")
				return(True)
		return(False)
			

	count = 1
	def iterdict_for_moves(d):
		########
		#  This function loops over passed in dictionaries and 
		# 		calculates further possible moves using all_moves().
		# 		Adds the newly created dictionary to the holder dictionaries.
		# 
		# 	Returns nothing.
		# 			just updates the holder dicts
		# 				
		########
		for v in list(d.values()):
			for i in v:
				temp = all_moves(i)
				if temp != ():
					# print("Temp.keys(): ", list(temp.keys())[0])
					# print("#"*20)
					if list(temp.keys())[0] not in master_dict_holder.keys():
						# print("Temp: ",temp)
						# print("+"*20)
						# print()
						master_dict_test_new.update(temp)
						master_dict_holder.update(temp)
		
		
					
		# if temp != ():
		# 	return("HELLO AGAIN",search_for_match(temp))

	# print("Feedback: ",any([search_for_match(v) for k,v in master_dict_test_old.items()]))
	if src_coords == dst_coords:
		return(0)
	if any([search_for_match(v) for k,v in master_dict_test_old.items()]):
		return(1)
	else:
		while not any([search_for_match(v) for k,v in master_dict_test_old.items()]):
			count += 1
			iterdict_for_moves(master_dict_test_old)
			# print("#"*50)
			master_dict_test_old = master_dict_test_new
			master_dict_test_new = {}
			# print()
			# print("~"*50)
			# print(list(master_dict_test_old.values()))
			# print("~"*50)
			# print()
			# for k,v in master_dict_test_old.items():
			# 		print("Key: ",k,"  Value: ",v)
			

			if any([search_for_match(v) for k,v in master_dict_test_old.items()]):
				# for k,v in master_dict_test_old.items():
				# 	print("Key: ",k,"  Value: ",v)
				# print(any([search_for_match(v) for k,v in master_dict_test_old.items()]))
				return(count)
				# print("+"*50)

		
		





answer(src,dst)