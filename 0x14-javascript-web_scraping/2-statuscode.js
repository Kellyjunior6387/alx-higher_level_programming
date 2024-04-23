#!/usr/bin/node

url = process.argv[2]

const request = require('request')
request(url, function (err, res, body) {
	if (err) {
		console.log(err);
	} else {
		console.log(`code: ${res.statusCode}`);
	}
});
