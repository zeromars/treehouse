/// <reference path="app.ts" />

// tsc *.ts -t es5 -d --watch

//optionally typed
var name:string = "Andrew";
var name = "Andrew";

interface IEmailable {
	name: string,
	email: string
}

function sendEmail(contact: IEmailable){
	console.log(`${contact.name} <${contact.email}>`);
}

sendEmail({name: "Andrew Chalkley", email: "andrew@teamtreehouse.com"});

var treehouse = new Company("Treehouse", "support@teamtreegouse.com");

sendEmail(treehouse);

var playlist = new Playlist();

var song1 = new Song("Smells like teen spirit", "Nirvana", "1:12");
var song2 = new Song("Smells like teen spirit2", "Nirvana2", "1:13");
var song3 = new Song("Smells like teen spirit3", "Nirvana3", "1:14");
var song4 = new Song("Smells like teen spirit4", "Nirvana4", "1:15");
var song5 = new Song("Smells like teen spirit5", "Nirvana5", "1:16");

playlist.add(song1);
playlist.add(song2);
playlist.add(song3);
playlist.add(song4);
playlist.add(song5);

var playlistElement = document.getElementById("playlist");

playlist.renderInElement(playlistElement);

var playbutton = document.getElementById('play');
playbutton.onclick = function(){
		playlist.play();
		playlist.renderInElement(playlistElement);
};