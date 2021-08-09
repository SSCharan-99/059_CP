# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.

import math
def fun_distance(x1, y1, x2, y2):
	a=int((y2-y1)*(y2-y1))
	b=int((x2-x1)*(x2-x1))
	res=math.sqrt(b+a)
	# your code goes here
	return int(res)