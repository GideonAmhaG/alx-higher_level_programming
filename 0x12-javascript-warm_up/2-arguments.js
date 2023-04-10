#!/usr/bin/node
let str;
const len = process.argv.length;
if (len < 3) {
  str = 'No argument';
} else if (len === 3) {
  str = 'Argument found';
} else {
  str = 'Arguments found';
}
console.log(str);
