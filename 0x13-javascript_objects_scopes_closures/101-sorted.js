#!/usr/bin/node
const dict = require('./101-data').dict;
const obj = {};
for (const value of Object.values(dict)) {
  const list = [];
  obj[value] = list;
  for (const [key, val] of Object.entries(dict)) {
    if (value === val) {
      list.push(key);
    }
  }
}
console.log(obj);
