# Doomsday Fuel
# =============

# Making fuel for the LAMBCHOP's reactor core is a tricky process because 
# of the exotic matter involved. It starts as raw ore, then during processing, 
# begins randomly changing between forms, eventually reaching a stable form. 
# There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

# Commander Lambda has tasked you to help the scientists increase fuel 
# creation efficiency by predicting the end state of a given ore sample. 
# You have carefully studied the different structures that the ore can take 
# and which transitions it undergoes. It appears that, while random, 
# the probability of each structure transforming is fixed. That is, each time 
# the ore is in 1 state, it has the same probabilities of entering the next state 
# (which might be the same state).  You have recorded the observed transitions in a 
# matrix. The others in the lab have hypothesized more exotic forms that the ore can 
# become, but you haven't seen all of them.

# Write a function answer(m) that takes an array of array of nonnegative 
# ints representing how many times that state has gone to the next state 
# and return an array of ints for each terminal state giving the exact 
# probabilities of each terminal state, represented as the numerator for 
# each state, then the denominator for all of them at the end and in simplest 
# form. The matrix is at most 10 by 10. It is guaranteed that no matter which 
# state the ore is in, there is a path from that state to a terminal state. That is, 
# the processing will always eventually end in a stable state. The ore starts in state 0. 
# The denominator will fit within a signed 32-bit integer during the calculation, 
# as long as the fraction is simplified regularly. 

# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# Output:
#     (int list) [7, 6, 8, 21]

# Inputs:
#     (int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# Output:
#     (int list) [0, 3, 2, 9, 14]

# Use verify [file] to test your solution and see how it does. 
# When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.







from fractions import Fraction, gcd
from functools import reduce

def answer(m):
	if len(m) == 1:
		return([1,1])

	##################################
	##### BEGIN HELPER FUNCTIONS #####
	 ################################

	def leastCommonMultiple(a,b):
		return a * b // gcd(a,b)

	def leastCommonMultMap(lis):
		return reduce(lambda x, y: leastCommonMultiple(x,y), lis)

	def transposeMatrix(m):
		m_transpose = []
		for row in range(len(m)):
			transpose_row = []
			for col in range(len(m[row])):
				if col == row:
					transpose_row.append(m[row][col])
				else:
					transpose_row.append(m[col][row])
			m_transpose.append(transpose_row)
		return m_transpose

	def MatrixMult(x,y):
		result = []

		for i in range(len(x)):
			result.append([])
			for j in range(len(y[0])):
				result[i].append(0)
				for k in range(len(y)):
					result[i][j] += x[i][k] * y[k][j]

		return (result)


	
	def MatrixMinor(m,i,j):
		return([row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])])
		
	def MatrixDeterminant(m):
		# base case for 2x2 matrices
		if len(m) == 2:
			determinant = (m[0][0]*m[1][1]) - (m[0][1]*m[1][0])
			return(determinant)

		determinant = 0
		for col in range(len(m)):
			#determinant =   sign    * each in row 1 
			determinant += ((-1)**col) * m[0][col] * MatrixDeterminant(MatrixMinor(m,0,col))
		return(determinant)



	def MatrixInverse(m):
		determinant = MatrixDeterminant(m)
		#special case for 2x2 matrix:
		if len(m) == 2:
			return([[m[1][1]/determinant, -1*m[0][1]/determinant],
					[-1*m[1][0]/determinant, m[0][0]/determinant]])

		#find matrix of cofactors
		cofactors = []
		for r in range(len(m)):
			cofactorRow = []
			for c in range(len(m)):
				minor = MatrixMinor(m,r,c)
				cofactorRow.append(((-1)**(r+c)) * MatrixDeterminant(minor))
			cofactors.append(cofactorRow)
		cofactors = transposeMatrix(cofactors)
		for r in range(len(cofactors)):
			for c in range(len(cofactors)):
				cofactors[r][c] = cofactors[r][c]/determinant
		return(cofactors)

	 ##############################
	##### END HELPER FUNCTIONS #####
	################################


	absorbing_states = []
	nonabsorbing_states = []
	absorbing_rows = []
	nonabsorbing_rows = []
	row_order = []
	size_of_Q = 0

	# Find the absorbing / nonabsorbing rows, place into seperate lists
	# 	Also find size of Q and index of rows for ordering later
	for i in range(len(m)):
		if sum(m[i]) > 0:
			nonabsorbing_rows.append(i)
			nonabsorbing_states.append(m[i])
			size_of_Q += 1
		else:
			absorbing_rows.append(i)
			absorbing_states.append(m[i])

	row_order = absorbing_rows + nonabsorbing_rows



	### Creating the limiting matrix

	# Append abosorbing rows first
	#	Add 1 to the col that equals it's row index
	# 		Forming Matrix(I) + Matrix(0)
	limiting_Matrix = []
	j = 0
	for i in absorbing_states:
		limiting_Matrix.append(i)
		limiting_Matrix[j][j] = 1
		j += 1 

	# Append nonabsorbing rows with columns reordered to match
	# 	absorbing rows first followed by nonabsorbing
	# Change values to Fractions instead of current count
	for i in nonabsorbing_rows:
		temp, temp2 = [], []
		for j in row_order:
			temp.append(m[i][j])
		for index, value in enumerate(temp):
			temp2.append(Fraction(value, sum(temp) ))  

		limiting_Matrix.append(temp2)

	if len(absorbing_states) == 1:
		return([1,1])

	# Create Q and R from limiting Matrix
	Q = [x[-size_of_Q:] for x in limiting_Matrix[-size_of_Q:]]
	R = [x[:-size_of_Q] for x in limiting_Matrix[-size_of_Q:]]

	# Create Identity matrix size of Q
	I = []
	for i in range(size_of_Q):
		I.append([])
		for j in range(size_of_Q):
			if i == j:
				I[i].append(1)
			else:
				I[i].append(0)

	# Subtract Q from I
	I_Q = []
	for i in range(size_of_Q):
		I_Q.append([])
		for j in range(size_of_Q):
			I_Q[i].append(I[i][j]-Q[i][j])


	# Find F = (I-Q)^-1  (inverse of I - Q)
	F = MatrixInverse(I_Q)

	# Find F * R
	FR = MatrixMult(F,R)

	# Take only the first row of Matrix(F*R)
	FR = FR[0]

	# Fractions to lists
	fractions_as_list = []
	for i in FR:
		fractions_as_list.append([i.numerator, i.denominator])

	# Find the Least Common Multiple(LCM) for list using denominators(i[1])
	lcm1 = leastCommonMultMap([i[1] for i in fractions_as_list])
	
	# Create list with all values having the same denominator
	ende = [ (lcm1//i[1]) * i[0] for i in fractions_as_list ]

	# Append the LCM to the list of numerators
	final_answer = ende + [lcm1]

	return (final_answer)


answer([
[0, 2, 1, 0, 0],
[0, 0, 0, 3, 4],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
])## == [7, 6, 8, 21]



answer([
[0, 1, 0, 0, 0, 1],
[4, 0, 0, 3, 2, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]
])# == [0, 3, 2, 9, 14]



answer([
[1, 2, 3, 0, 0, 0],
[4, 5, 6, 0, 0, 0],
[7, 8, 9, 1, 0, 0],
[0, 0, 0, 0, 1, 2],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]
])# == [1, 2, 3]


answer([
[0]
])# == [1, 1]



answer([
[0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
[0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
[0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
[23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])# == [1, 2, 3, 4, 5, 15]



answer([
[0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
[0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
[0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
[48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
[0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])# == [4, 5, 5, 4, 2, 20]



answer([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])# == [1, 1, 1, 1, 1, 5]



answer([
[1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])# == [2, 1, 1, 1, 1, 6]



answer([
[0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
[0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
[15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])# == [6, 44, 4, 11, 22, 13, 100]



answer([
[0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
[0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
[13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
[0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
[1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])# == [1, 1, 1, 2, 5]

