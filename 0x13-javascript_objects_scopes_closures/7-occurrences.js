#!/usr/bin/node

 exports.nbOccurences = function (list, searchElement) {
	 let count = 0;
	 for (let element in list){
		 if (element === searchElement){
			 count++;
		 }
	 }
	 return count;
 };
