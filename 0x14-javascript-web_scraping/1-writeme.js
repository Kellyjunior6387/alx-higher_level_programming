#!/usr/bin/node

file_path = process.argv[2]
content = process.argv[3]

const fs = require("fs")
fs.writeFile(file_path, content, 'utf-8', (err) => {
	if (err) {
		console.log(err);
	}
});
