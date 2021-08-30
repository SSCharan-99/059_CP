# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 

def binary_search2(arr,low,l,x,res):
	
	if l >= low:

		m = (l + low) // 2
		print('midval',m,'lowval',low,'highval',l)
		if arr[m] == x:
			temp = (m, arr[m])
			print(temp)
			res.append(temp)
			return res
			

		elif arr[m] > x:
			temp = (m, arr[m])
			print(temp)
			res.append(temp)
			return binary_search2(arr, low, m - 1, x, res) 
		else:
			temp = (m, arr[m])
			print(temp)
			res.append(temp)
			return binary_search2(arr, m + 1, l, x, res) 
	else:
		return res


def recursion_binarysearchvalues(L, v):
	res =[]
	# Your codes goes here
	arr = L
	low = 0
	l = len(L)-1
	x = v
	return binary_search2(arr,low,l,x,res)