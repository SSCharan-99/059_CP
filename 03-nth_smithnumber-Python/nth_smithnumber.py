# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def factors(n):
    rt = []
    f = 2
    if n == 1:
        rt.append(1)
    else:
        while 1:
            if 0 == ( n % f ):
                rt.append(f)
                n //= f
                if n == 1:
                    return rt
            else:
                f += 1
    return rt
 
 
def sum_digits(n):
    sum = 0
    while n > 0:
        m = n % 10
        sum += m
        n -= m
        n //= 10
 
    return sum
 
 
def add_all_digits(lst):
    sum = 0
    for i in range (len(lst)):
        sum += sum_digits(lst[i])
 
    return sum

def isSmith(i):
    fac = factors(i)
    if len(fac) > 1 and sum_digits(i) == add_all_digits(fac):
        return True
    return False

def fun_nth_smithnumber(n):
	count=0
	i=1
	while(count<=n):
		if isSmith(i):
			count+=1
		i=i+1
	return i-1