# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

import math

def chunk (array, size):
	rows = 0
	l = len(array)

	if l % size == 0:
		rows = l/size
	else:
		rows = int(math.floor(l/size) + 1)


	m_list = ['' for e in range(size)]
	print 'Debug---m_list: ' + str(m_list)

	m_matrix = [['' for g in range(size)] for w in range(rows)]
	print 'Debug---m_matrix: ' + str(m_matrix)

	i = 0

	for r in range(rows):
		for u in range(size):
			if i == l:
				print 'breakkkkk: ' + str(i)
				# m_list = [0 for z in range(size)]
				print '@@@@@-m_list: ' + str(m_list)
				break
			else: 
				m_list[u] = array[i]
				print 'Debug---m_list: ' + str(m_list)
				i += 1
				print 'index i: ' + str(i)

		m_matrix[r] = m_list
		print '**debug: ' + str(m_matrix[r])

	print '$$$-debug: ' + str(m_matrix)
	return m_matrix


###############################################


def x_chunk(inputarray,size):

    array = inputarray
    m_matrix = []


    while len(array) > 0:
        if len(array[:size]) < size:
            array.extend(['' for j in range(size-len(array[:size]))])
        m_matrix.append(array[:size])
        del array[:size]


    return m_matrix









length = int(raw_input('how many elements you want in the array?: '))

m_inputArray = ['' for q in range(length)]
print 'Debug0:--> ' + str(m_inputArray)
for z in range(length):
	p = int(raw_input('Enter the value at index %i :' %(z)))	
	m_inputArray[z] = p

m_inputSize = int(raw_input('Enter the size: '))


result = x_chunk(m_inputArray, m_inputSize)
print result
 
