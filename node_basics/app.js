console.log("Hello World!");

/**
--Notes--
repl = read edit print loops

Javascript engine
Native objects = String , Array , Date , Math //can use anywhere
Host Objects = Window , Document, History , XMLHttpRequest = Browser
Host Objects = http, https, fs (file system), url = Node Console (v8)

4P's of proglem solving
Preperation
Plan
Perform
Perfect

Adding .json to a profile gets you a api endpoint

If you're done adding additional functionality to this project, why not create a command line application that takes a Zip Code or Postal Code and it retrieves the forecast for today.

For example:

node forecast.js 90210
Forecast.io has an API you could use.

**/

//Problem: we need a simple way to look at a users badge count and javascript points
//Use nodejs to connect to treehouses api to get profile information and print it out
var profile = require("./profile.js");
//var profile = require("./profile"); //or this
//console.dir(process);
//console.dir(process.argv);
//var users = ['landonlung', 'chalkers'];
var users = process.argv.slice(2);

users.forEach(function(username){
	profile.get(username);
});