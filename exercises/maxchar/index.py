# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

def maxChar(m_str):
	m_list = list(m_str)
	m_uniqueChars = ['' for j in range(len(m_list))]
	m_noOfRepeats = [0 for j in range(len(m_list))]
	m_maxCount = 0
	m_maxIndex = 0

	for i in range(len(m_list)):
		# print 'Debug0:' + str(i)					# debug OK
		for j in range (i+1):
			if m_list[i] == m_uniqueChars[j]:
				m_noOfRepeats[j] +=1
				# print 'Debug1:' + str(j)			# debug
				break
			else:
				if j==i or i==0:
					m_uniqueChars[i] = m_list[i]
					m_noOfRepeats[i] += 1
				j+=1
		i+=1


	for k in range(len(m_noOfRepeats)):
		if m_noOfRepeats[k] == 0:
			break
		if m_noOfRepeats[k] > m_maxCount:
			m_maxCount = m_noOfRepeats[k]
			m_maxIndex = k
		else:
			k+=1
			
	return m_uniqueChars[m_maxIndex]


x = raw_input('Enter the string: ')
result = maxChar(x)
print result