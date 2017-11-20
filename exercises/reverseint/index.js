// --- Directions
// Given an integer, return an integer that is the reverse
// ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9

function reverseInt(n) {
	const m_reversed =  n.toString().split('').reverse().join('');
	m_revInteger = parseInt(m_reversed);

	return m_revInteger * Math.sign(n);
}

module.exports = reverseInt;


/*function reverseInt(n) {
	const m_reversed =  n.toString().split('').reverse().join('');
	m_revInteger = parseInt(m_reversed);

	if (n < 0){
		return -1 * m_revInteger;
	}
	else{
		return m_revInteger;
	}
}*/