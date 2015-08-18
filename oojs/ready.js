var dice = {
	sides: 6,
	roll: function diceRoll() {
	  var sides = dice.sides;
	  var randomNumber = Math.floor(Math.random() * sides) + 1;
	  console.log(randomNumber);

	  return randomNumber;
	}
}

function Dice(num){
	this.sides =  num;
}

Dice.prototype.roll = function() {
  var sides = dice.sides;
  var randomNumber = Math.floor(Math.random() * sides) + 1;
  console.log(randomNumber);

  return randomNumber;
}

var rollMe = new Dice(7);

function printNumber(number) {
  var placeholder = document.getElementById("placeholder");
  placeholder.innerHTML = number;
}

var button = document.getElementById("button");

button.onclick = function() {
  var result = dice.roll();
  printNumber(result);
};

var calculator = {
  sum: 0,
  add: function(value) {
    this.sum += value;
  },
  subtract: function(value) {
    this.sum -= value;
  },
  multiply: function(value) {
    this.sum = this.sum * value;
  },
  divide: function(value) {
    this.sum = this.sum / value;
  },
  clear: function() {
    this.sum = 0;
  }, 
  equals: function() {
    return this.sum;
  }
}

function Playlist() {
	this.songs = [];
	this.nowPlayingIndex = 0;
}

Playlist.prototype.add = function(song) {
	this.songs.push(song);
};

Playlist.prototype.play = function() {
	var currentSong = this.songs[this.nowPlayingIndex];
	console.log(this.nowPlayingIndex);
	console.log(currentSong);
	currentSong.play();
};

Playlist.prototype.stop = function(){
	var currentSong = this.songs[this.nowPlayingIndex];
	console.log(currentSong);
	currentSong.stop();
};

Playlist.prototype.next = function() {
	this.stop();
	this.nowPlayingIndex++;
	if(this.nowPlayingIndex == this.songs.length){
		this.nowPlayingIndex = 0;
	}
	this.play();
};

Playlist.prototype.renderInElement = function(list) {
	list.innerHTML = '';
	for(var i=0; i< this.songs.length; i++){
		list.innerHTML += this.songs[i].toHTML();
	}
};


function Media(title, duration) {
	this.title = title;
	this.duration = duration;
	this.isPlaying = false;
}

Media.prototype.play = function() {
	this.isPlaying = true;
};

Media.prototype.stop = function() {
	this.isPlaying = false;
};
function Song(title, artist, duration) {
	Media.call(this, title, duration);
	this.artist = artist;	
	/*this.title = title;
	this.duration = duration;
	this.isPlaying = false;*/
}

Song.prototype = Object.create(Media.prototype);

/*
Song.prototype.play = function() {
	console.log('im not getting called');
	this.isPlaying = true;
};

Song.prototype.stop = function() {
	this.isPlaying = false;
};
*/
Song.prototype.toHTML = function() {
	var html = '<li class="'+ (this.isPlaying ? "current" : "") + '">'+this.title+ ' - ' + this.artist + ' <span class="duration">'+this.duration+'</span></li>';
	return html;
};


function Movie(title, year, duration) {
	Media.call(this, title, duration);
	this.year = year;	
	/*this.title = title;
	this.duration = duration;
	this.isPlaying = false;*/
}

Movie.prototype = Object.create(Media.prototype);

Movie.prototype.toHTML = function() {
	var html = '<li class="'+ (this.isPlaying ? "current" : "") + '">'+this.title+ ' - ' + this.year + ' <span class="duration">'+this.duration+'</span></li>';
	return html;
};

var playlist = new Playlist();

var dirtymaxx = new Song("DirtyMaxxx","Young Gunner","4:50");
var bounce = new Song("Bounce","Redneck Solijers","2:50");
var superman = new Movie("Superman","1999","1:10");

playlist.add(dirtymaxx);
playlist.add(bounce);
playlist.add(superman);

var playlistElement = document.getElementById("playlist");
playlist.renderInElement(playlistElement);

var playButton = document.getElementById("play");
playButton.onclick = function(){
	playlist.play();
	playlist.renderInElement(playlistElement);
};
var nextButton = document.getElementById("next");
nextButton.onclick = function(){
	playlist.next();
	playlist.renderInElement(playlistElement);
};
var stopButton = document.getElementById("stop");
stopButton.onclick = function(){
	playlist.stop();
	playlist.renderInElement(playlistElement);
};