// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(my_str) {
	return my_str.split('').reduce((my_reversed, my_character) => {
		return my_character + my_reversed;
	}, '');
}

module.exports = reverse;

/*function reverse(str) {
	let reversed = '';

	for (let character of str){
		reversed = character + reversed;
		// reversed = reversed + character; //this will append characters of str from right side of reversed
		console.log(reversed);
	}

	return reversed;

}*/

/*function reverse(str) {
	const arr = str.split('');
	arr.reverse();
	return arr.join('');
}
*/