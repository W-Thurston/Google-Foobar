# Numbers Station Coded Messages
# ==============================

# When you went undercover in Commander Lambda's organization, 
# you set up a coded messaging system with Bunny Headquarters to allow 
# them to send you important mission updates. Now that you're here and 
# promoted to Henchman, you need to make sure you can receive those 
# messages - but since you need to sneak them past Commander Lambda's spies, it won't be easy!

# Bunny HQ has secretly taken control of two of the galaxy's more obscure numbers stations,
 # and will use them to broadcast lists of numbers. They've given you a numerical key,
  # and their messages will be encrypted within the first sequence of numbers that adds up
   # to that key within any given list of numbers. 

# Given a non-empty list of positive integers l and a target positive integer t, 
# write a function answer(l, t) which verifies if there is at least one consecutive 
# sequence of positive integers within the list l (i.e. a contiguous sub-list) that can 
# be summed up to the given target positive integer t (the key) and returns the 
# lexicographically smallest list containing the smallest start and end indexes where 
# this sequence can be found, or returns the array [-1, -1] in the case that there is no 
# such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).

# For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, 
# the function answer(l, t) would return the list [0, 2] because the list l contains 
# the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, 
# even though there is a shorter sequence that happens later in the list (5 + 7). On the other hand, 
# given the list l as [1, 2, 3, 4] and the key t as 15, the function answer(l, t) would return [-1, -1] 
# because there is no sub-list of list l that can be summed up to the given target value t = 15.

# To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards: 

# - Each list l will contain at least 1 element but never more than 100.
# - Each element of l will be between 1 and 100.
# - t will be a positive integer, not exceeding 250.
# - The first element of the list l has index 0. 
# - For the list returned by answer(l, t), the start index must be equal or smaller than the end index. 

# Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous sublist 
# of a number broadcast that can be summed up to the key. You know that the message will always be 
# hidden in the first sublist that sums up to the key, so answer(l, t) should only return that sublist.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int list) l = [4, 3, 10, 2, 8]
#     (int) t = 12
# Output:
#     (int list) [2, 3]

# Inputs:
#     (int list) l = [1, 2, 3, 4]
#     (int) t = 15
# Output:
#     (int list) [-1, -1]

# Use verify [file] to test your solution and see how it does. 
# When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.



def answer(l,t):
	######
	# The function calulates sums for all sub strings in given list l
	# 	Then tests to see if that sum is equal to integer t
	# 
	# Returns:
	# 		The smallest sum of index range:
	# 			ex:	l = [4, 3, 5, 7, 8]
	# 				t = 12
	# 				sum([4,3,5]) = 12  -> index([0,2]) -> sum = 2
	# 				sum([5,7]) = 12    -> index([2,3]) -> sum = 5
	# 				
	# 				Returns [0,2]
	# 
	# 		If no substring found retrun [-1,-1]
	######



	found_flag  = False
	all_solved  = []
	all_index   = []
	sum_indexes = []

	# Loop through each substring of list l
	# 	If found set found_flag to True & append indexes to holder list
	for i in range(len(l)):
		for j in range(1,len(l)-i+1):
			sub = l[i:i+j]
			if sum(sub) == t:
				found_flag = True
				# all_solved.append(sub)
				all_index.append([i,i+j-1])
				
	# Calculate sum of each set of indexes
	for i in all_index:
		sum_indexes.append(sum(i))

	# use minimum value's index of sum_indexes as index to find
	#	 substring indexes
	if found_flag:
		return( all_index[sum_indexes.index(min(sum_indexes))] )
	else:

		return([-1,-1])







######## Test function

l = [4, 3, 5, 7, 8]
t = 12
answer(l,t)


l = [4, 3, 10, 2, 8,4, 3, 10, 2, 8]
t = 12
answer(l,t)


l = [1, 2, 3, 4]
t = 15
answer(l,t)