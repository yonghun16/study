/* Call Signatures */
console.log()
console.log('/* Call Signatures */');

type Add = (a: number, b: number) => number

const add: Add = (a, b) => a + b;

console.log(add(3, 5));
