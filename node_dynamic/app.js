//Problem: we need a simple way to look at a users badge count and javascript points from a web browser.
//Solution: use nodejs to preform the profile lookups and serve our templates via http.

/*
Killing process
$ ps -aux
$ kill -9 <process id/PID from ps>
*/

// 1.) Create a webserver
var router = require('./router');
var render = require('./render');
var http = require('http');
http.createServer(function (req, res) {
  router.home(req, res);
  router.user(req, res);
}).listen(1337, '127.0.0.1'); //second param is optional
console.log('Server running at http://127.0.0.1:1337/');