const h1 = /^# (.*$)/gim 
const h2 = /^## (.*$)/gim 
const h3 = /^### (.*$)/gim 
const boldAsterisk = /\*\*(.*)\*\*/gim
const boldUnderscore = /\_\_(.*)\_\_/gim
const italicsAsterisk = /\*(.*)\*/gim
const italicsUnderscore = /\_(.*)\_/gim

export default function markdownParser(text) {
  const toHTML = text
		.replace(h1, '<h1>$1</h1>') // h1 tag
		.replace(h2, '<h2>$1</h2>') // h2 tag
		.replace(h3, '<h3>$1</h3>') // h3 tag
		.replace(boldAsterisk, '<b>$1</b>') // boldAsterisk text
		.replace(boldUnderscore, '<b>$1</b>') // boldUnderscore text
		.replace(italicsAsterisk, '<i>$1</i>') // italicsAsterisk text
		.replace(italicsUnderscore, '<i>$1</i>'); // italicsUnderscore text
	
  return toHTML.trim(); // using trim method to remove whitespace
};