# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property309(n):
	temp=["0","1","2","3","4","5","6","7","8","9"]
	count=0
	res=n**5
	res=str(res)
	res1=set(res)

	res2=list(res1)
	res2.sort()

	for i in range(len(res2)):
	    if res2[i] in temp:
	        count=count+1
	if count==10:
	    return True
	return False


def nthwithproperty309(n):

	count=0
	i=0
	while(count<=n):
		if property309(i):
			count+=1
		i=i+1
	return i-1