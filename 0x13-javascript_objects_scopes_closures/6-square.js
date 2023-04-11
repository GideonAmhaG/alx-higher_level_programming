#!/usr/bin/node
const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  charPrint (c = 'X') {
    super.print(c);
  }
};
