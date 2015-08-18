var Profile = require("./profile.js");
var render = require("./render");
var qs = require('querystring');
var commonHeader = "{'Content-Type': 'text/html'}";

//get = makes it a query strings
//post = sends it in the request body

// 2.) Handle http route GET / and POST i.e. Home
function home(req, res){
	//if url == "/" and GET
	//console.log(req);
	//console.log(req.url === "/");
	if(req.url === "/"){
		if(req.method.toLowerCase() === "get"){
			//show search
			//res.writeHead(200, {'Content-Type': 'text/plain'});
			res.writeHead(200, commonHeader);	
			/*
			setInterval(function(){
				res.write(new Date() + '\n');
			}, 1000);
			res.write('This is before the end.\n');
			//res.end('Hello World\n');
			res.write('This is after the end.\n'); //not rendered
			*/
			//res.write('Header\n');
			render.view("header", {}, res);	
			render.view("search", {}, res);	
			render.view("footer", {}, res);	
			res.end();
		}else{
			//if url is "/" and POST
			//get post data from body
			req.on('data', function(postBody){
				//console.log(postBody.toString());
				//extract username
				var query = qs.parse(postBody.toString());
				//res.write(query.username);
				//redirect to /:username
				res.writeHead(303, {Location: "/" + query.username});
				//end response
				res.end();
			});
		}
	}
}

// 3.) Handle http route GET /:username i.e. landonlung
function user(req, res){
	// if url == "/...."
	var username = req.url.replace("/", "");
	if(username.length > 0){
		//res.writeHead(200, {'Content-Type': 'text/plain'});
		res.writeHead(200, commonHeader);
		//res.write('Header\n');
		render.view("header", {}, res);	

		//get json from treehouse
		var studentProfile = new Profile(username);
		//on end
		//show profile
		studentProfile.on("end", function(profileJSON){
			//show profile

			//Store the values which we need
			var values = {
				avatarUrl: profileJSON.gravatar_url,
				username: profileJSON.profile_name,
				badges: profileJSON.badges.length,
				points: profileJSON.points.JavaScript
			};
			//simple response
			render.view("profile", values, res);	
			render.view("footer", {}, res);	
			res.end();
		});
		//on error 
		//show error
		studentProfile.on("error", function(error){
			//show error
			render.view("error", {errorMessage: error.errorMessage}, res);	
			render.view("search", {}, res);	
			render.view("footer", {}, res);	
			res.end();
		});
	}
}

module.exports.home = home;
module.exports.user = user;