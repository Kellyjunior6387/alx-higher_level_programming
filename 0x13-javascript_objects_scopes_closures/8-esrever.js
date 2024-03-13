#!/usr/bin/node

exports.esrever = function(list) {
	let word = [];
	for (let i = list.length - 1; i >= 0; i--) {
		word.push(list[i]);
	}
	return word;
};
