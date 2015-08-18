var http = require("http");
//print out message
function printMessage (username, badgeCount, points){
	var message = username + " has " + badgeCount + " total badge(s) and " + points + " points in Javascript.";

	console.log(message);
}

//print out error message
function printError(e){
	console.error("Got error: " + e.message);
}

function get(username){
	//connect to api url
	var request = http.get("http://teamtreehouse.com/"+username+".json" , function(response) {
		//console.dir(response);
	  	console.log("Got response: " + response.statusCode);
	  	var body = "";
		//read the data
		response.on('data', function (chunk) {
			//console.log('BODY: ' + chunk);
			body += chunk;
		});
		response.on('end', function(){
			//console.log(body);
			//console.log(typeof(body));
			if(response.statusCode === 200){
				try {
					var profile = JSON.parse(body);
					//console.dir(profile);
					printMessage(username, profile.badges.length, profile.points.JavaScript);
				} catch(error){
					//parse error
					printError(error);
				}
			}else{
				//Status code error
				printError({message: 'There was a profile for that user ['+response.statusCode+': ' + [http.STATUS_CODES[response.statusCode]] + ']'});
			}
			//console.dir(profile.badges.length);
			//console.dir(profile.points.JavaScript);
		});
		//parse the data
		//print the data
		//connection error
	}).on('error', printError);
}

module.exports.get = get;