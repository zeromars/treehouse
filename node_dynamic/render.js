// 4.) Function that handles the reading of files and merge in values.
	//read from file and get a string
		// merge values into string
var fs = require('fs');

function mergeValues(values, content){
	//cycle over the keys
	for(var key in values){
		//replace all {{key}} from values

		//values.key doesnt work here
		content = content.replace("{{" + key + "}}", values[key]);
	}
	//return merge content
	return content;
}

function view(template, values, res){
	//read from template file

	//fs.readFile('./views/' + template + ".html", function (err, data) { //async
	//fs.readFileSync('./views/' + template + ".html", function (err, data) {

	/*
	fs.readFile('./views/' + template + ".html", function (err, data) {
	  if (err) throw err;
	  //console.log(data);
	  res.write(data);
	});
	*/
	var data = fs.readFileSync('./views/' + template + ".html", {encoding: 'utf8'});

	//insert values into content
	data = mergeValues(values, data)

	//write out to the response	
	res.write(data);
}

module.exports.view = view;