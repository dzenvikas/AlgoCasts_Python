# --- Directions
# Write a program that console logs the numbers
# from 1 to n. But for multiples of three print
# 'fizz' instead of the number and for the multiples
# of five print 'buzz'. For numbers which are multiples
# of both three and five print 'fizzbuzz'.
# --- Example
#   fizzBuzz(5);
#   1
#   2
#   fizz
#   4
#   buzz


def fizzbuzz (n):			# n ---> whole number
	a = int(n)
	i = 1
	
	while i <= a:
		if i % 3 == 0 and i % 5 == 0:	# check if number is divisible by 3 and 5 both
			print 'fizzbuzz'
		elif i % 3 == 0:				# check if number is divisible by 3
			print 'fizz'
		elif i % 5 == 0:				# check if number is divisible by 5
			print 'buzz'
		else:
			print i

		i += 1							# increment count


x = raw_input('Enter whole number: ')
result = fizzbuzz(x)