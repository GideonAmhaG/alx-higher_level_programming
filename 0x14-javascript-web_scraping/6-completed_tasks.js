#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  !error && console.log(JSON.parse(body).reduce(function (all, cur) {
    cur.completed && (all[cur.userId] = (all[cur.userId] || 0) + 1);
    return all;
  }, {}));
});
