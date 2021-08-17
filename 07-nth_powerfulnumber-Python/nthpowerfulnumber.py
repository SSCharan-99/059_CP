# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
def get_prime_factors(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n>1:
        prime_factors.append(n)
    
    return prime_factors

def is_powerful(n):

    prime_factors = get_prime_factors(n)

    unique_prime = tuple(dict.fromkeys(prime_factors))
    for p in unique_prime:
        if n % p != 0 or n % (p*p) != 0:
            return False
    return True
	


def nthpowerfulnumber(n):
	# Your code goes here
	count=0
	i=1
	if(n==0):
		return 1
	while(count<=n):
		if is_powerful(i):
			count=count+1
		i=i+1
	return i-1
