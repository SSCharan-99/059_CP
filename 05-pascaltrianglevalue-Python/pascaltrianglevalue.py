# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 



import math
def fun_pascaltrianglevalue(row, col):
	if (row<0 or col<0 or col>row):
		return 0
	else:
		res1=math.factorial(row)
		res2=math.factorial(col)
		ans=math.factorial(row-col)
		fin= res1//(res2*ans)
		return fin