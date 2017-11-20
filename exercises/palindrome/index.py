 # --- Directions
 # Given a string, return true if the string is a palindrome
 # or false if it is not.  Palindromes are strings that
 # form the same word if it is reversed. *Do* include spaces
 # and punctuation in determining if the string is a palindrome.
 # --- Examples:
 #   palindrome("abba") === true
 #   palindrome("abcdefg") === false

# reverse a string
def palindrome(my_str):
	p = True
 	counter = 0
 	l = len(my_str)
 	my_reversed = [j for j in range(l)]

 	while counter < l:
 		my_reversed[counter] = my_str[(l-1)-counter]
 		counter+=1

 	rev = ''.join(my_reversed)
 	print 'Debug: rev = ' + rev
 	
# checks if my_str string is palidrome or not and return boolean
	for counter in range(l):
		if rev[counter] != my_str[counter]:
			p = False
			break
		else:
			counter+=1

	return p


# input from user
x = raw_input('Enter string: ')
# invoke def palindrome
result = palindrome(x)
print result