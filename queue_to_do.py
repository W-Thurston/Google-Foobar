# Queue To Do
# ===========

# You're almost ready to make your move to destroy the LAMBCHOP doomsday device,
# but the security checkpoints that guard the underlying systems of the LAMBCHOP
# are going to be a problem. You were able to take one down without tripping any alarms, 
# which is great! Except that as Commander Lambda's assistant, you've learned that the 
# checkpoints are about to come under automated review, which means that your sabotage will 
# be discovered and your cover blown - unless you can trick the automated review system.

# To trick the system, you'll need to write a program to return the same security 
# checksum that the guards would have after they would have checked all the workers through. 
# Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, 
# so the checkpoint guards have found ways to quicken the pass-through rate. Instead of checking 
# each and every worker coming through, the guards instead go over everyone in line while noting 
# their security IDs, then allow the line to fill back up. Once they've done that they go over the 
# line again, this time leaving off the last worker. They continue doing this, leaving off one 
# more worker from the line each time but recording the security IDs of those they do check, 
# until they skip the entire line, at which point they XOR the IDs of all the workers they noted 
# into a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them 
# to always line up in numerical order without any gaps.

# For example, if the first worker in line has ID 0 and the security checkpoint 
# line holds three workers, the process would look like this:
# 0 1 2 /
# 3 4 / 5
# 6 / 7 8
# where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.

# Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
# 17 18 19 20 /
# 21 22 23 / 24
# 25 26 / 27 28
# 29 / 30 31 32
# which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

# All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, 
# and the checkpoint line will always be at least 1 worker long.

# With this information, write a function answer(start, length) that will cover for 
# the missing security checkpoint by outputting the same checksum the guards would 
# normally submit before lunch. You have just enough time to find out the ID of the 
# first worker to be checked (start) and the length of the line (length) before the 
# automatic review occurs, so your program must generate the proper checksum with just those two values.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) start = 0
#     (int) length = 3
# Output:
#     (int) 2

# Inputs:
#     (int) start = 17
#     (int) length = 4
# Output:
#     (int) 14

# Use verify [file] to test your solution and see how it does. 
# When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.





from functools import reduce
import operator

def answer(start, length):

	def find_base(start,size):
		ret_list = []
		if size == 1:
			return([start])
		if start == 0 and size == 0:
			return([0])

		# if start is even
		if start % 2 == 0:
			# size is even
			if size % 2 == 0:
				# size//2 is odd
				if (size//2) % 2 != 0:
					ret_list = [1]
					# ret_list.extend([0 for x in range( (size//2)//2  )])
					# ret_list.append(1)
					
				# size//2 is even
				# else:
					# pass
					# ret_list = [0 for x in range( (size//2)//2  )]
					# ret_list.extend([0 for x in range( (size//2)//2  )])
					
			# size is odd
			else:
				if (size//2) % 2 == 0:
					ret_list = [start+size-1]
					# ret_list.extend([0 for x in range( (size//2)//2  )])
					# ret_list.append(start+size-1)
				else:
					ret_list = [1, start+size-1]
					# ret_list.extend([0 for x in range( (size//2)//2  )])
					# ret_list.append(1)
					# ret_list.append(start+size-1)

		# else start is odd
		else:
			ret_list = [start]
			# size is even
			if size % 2 == 0:
				# size//2 is even
				if (size//2) % 2 == 0:
					if size-2 > 2:
						if (size-2)//2 % 2 != 0:
							ret_list.extend([1, start+size-1])
							# ret_list.extend([0 for x in range( ((size//2)//2)-1 )])
							# ret_list.append(1)
							# ret_list.append(start+size-1)
						# else:
						# 	ret_list.extend([0 for x in range( (size-2)//2 )])
					else:
						ret_list.extend([1 for x in range( (size-2)//2 )])
						ret_list.append(start+size-1)
				# size//2 is odd
				else:
					ret_list.append(start+size-1)
					# ret_list.extend([0 for x in range( (size//2)//2  )])
					# ret_list.append(start+size-1)
			# size is odd
			else:
				if (size-1)//2 % 2 != 0:
					ret_list.append(1)
					# ret_list.extend([0 for x in range( ((size-1)//2)//2  )])
					# ret_list.append(1)
				# else:
				# 	ret_list.extend([0 for x in range( ((size-1)//2)//2  )])

		if ret_list == []:
			ret_list = [0]
		
		return(ret_list)

	# intialize checksum
	checksum = 0

	# Loop over length, decreasing its size each time to match
	#	"Leaving off one more worker each time"
	for size in range(length, 0 , -1):
		
		numbers_lis = [x for x in range(start, start+size)]
		print("Num list: ",numbers_lis)
		final = find_base(start,size)
		print(final)
		if final == [0]:
			start += length
			continue

		checksum ^= reduce(operator.xor, final)
		print("Checksum:", checksum)
		start += length

	print(checksum)
	print("#"*50)
	print()
	return checksum


		# perform XOR with previous checksum and XOR of
		# 	range of each new line. and increase start by length.
		#	ex: [0,1,2,/] -> XOR = 3 || checksum = 0, 0 XOR 3 = 3
		# 		[3,4,/,5] -> XOR = 7 || checksum = 3, 3 XOR 7 = 4
		#		[6,/,7,8] -> XOR = 6 || checksum = 4, 4 XOR 6 = 2 <- final
	






# answer(0, 22)
# answer(2, 12)
# answer(2, 15)
# answer(4, 13)

# answer(17, 22)
# answer(11, 12)
# answer(15, 13)
# answer(15, 15)

answer(0,3)
# answer(17,4)

# 	