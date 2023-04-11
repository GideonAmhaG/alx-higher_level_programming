#!/usr/bin/node
const fs = require('fs');
const contentA = fs.readFileSync(process.argv[2]);
const contentB = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], contentA + contentB);
