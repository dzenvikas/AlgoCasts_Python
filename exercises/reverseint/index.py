 # --- Directions
 # Given an integer, return an integer that is the reverse
 # ordering of numbers.
 # --- Examples
 #   reverseInt(15) === 51
 #   reverseInt(981) === 189
 #   reverseInt(500) === 5
 #   reverseInt(-15) === -51
 #   reverseInt(-90) === -9

# import math

# returns reversed positive integer
def reversePositiveInt(n):
 	s = str(n)
 	l = list(s)
 	rev = [j for j in range(len(l))]
 	i = 0 								#counter

 	while i < len(l):
 		rev[i] = l[len(l)-1-i]
 		# print 'Debug1: ' + rev[i] 	#debug
 		i+=1

 	return int(''.join(rev))			#converts list into string 

# reverse integer
def reverseInt(a):
	if a < 0:
		x = -1*a
		y = reversePositiveInt(x)
		return -1*y

	else:
		y = reversePositiveInt(a)
		return y


# testing
x = raw_input('Enter an integer: ')
result = reverseInt(int(x))				# invoke	
print result