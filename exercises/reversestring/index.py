# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'leppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'

# function to reverse the input of any typw
def reverse(my_str):
	print my_str
	l = len(my_str)
	print l
	i = 0
	y = [j for j in range(l)]
	print i
	print y

	while i < l:
		y[i] = my_str[(l-1)-i]
		print y[i]
		i+=1

	z = ''.join(y) # converts list into string

	print z

user_input = raw_input('Enter something: ')
# reverse('abcdef')
reverse(user_input) #func call