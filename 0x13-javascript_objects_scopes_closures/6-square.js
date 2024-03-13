const Square = require('./5-square')

class Square extends Square {
	charPrint(c) {
		if (c == undefined)
			c = 'X';
		let row = c.repeat(this.width);
		for (let i = 0; i < this.height; i++) {
			console.log(row);
		}
	}
}
