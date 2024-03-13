#!/usr/bin/node
const dict = require('./101-data').dict;

const newdict = [];

for (const id in dict) {
	const occur = dict[id];
	if (!(occur in newdict)) {
		newdict[occur] = [];
	}
	newdict[occur].push(id);
}
console.log(newdict);
