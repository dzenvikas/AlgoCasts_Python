// --- Directions
// Write a program that console logs the numbers
// from 1 to n. But for multiples of three print
// “fizz” instead of the number and for the multiples
// of five print “buzz”. For numbers which are multiples
// of both three and five print “fizzbuzz”.
// --- Example
//   fizzBuzz(5);
//   1
//   2
//   fizz
//   4
//   buzz

function fizzBuzz(n) {			// JavaScript takes n as integer...

	// var a = parseInt(n);		//...so we don't need to parse n

	for (var i = 1; i <= n;) {
		if (i % 3 === 0 && i % 5 ===0) {		// check if number is divisible by 3 and 5 both
			console.log('fizzbuzz');
		} else if ( i % 3 === 0) {				// check if number is divisible by 3
			console.log('fizz');
		} else if ( i % 5 === 0){				// check if number is divisible by 5
			console.log('buzz');
		} else {
			console.log(i);
		}

		i++;					// incerment count
	}

}

module.exports = fizzBuzz;
