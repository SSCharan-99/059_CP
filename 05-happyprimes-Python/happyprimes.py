# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def square(n):
	res = 0
	while(n):
		res += (n % 10) * (n % 10)
		n = int(n / 10)
	return res

def isprime(n):
    if n > 1:
        for i in range(2,int(n/2)+1):
            if (n % i == 0):
                return False
            else:
                return True

    else:
        return False

def ishappyprimenumber(n):
    slow = n
    fast = n
    while(True):
        slow = square(slow)
        fast = square(square(fast))
        if(slow != fast):
            continue
        else:
            break
    if (slow==1 and isprime(n)):
        return True
    return False
