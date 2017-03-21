/// <reference path="song.ts" />

class Playlist {
	songs: Song[];
	nowPlayingIndex: number;
	
	constructor(){
		this.songs = [];
		this.nowPlayingIndex = 0;
	}
	
	add(song: Song) {
		this.songs.push(song);
	}
	
	play() {
		this.currentSong.play();
	}
	
	stop() {
		this.currentSong.stop();
	}
	
	get currentSong(){
		return this.songs[this.nowPlayingIndex];
	}
	
	next(){
		this.stop();
		this.nowPlayingIndex++;
		if(this.nowPlayingIndex === this.songs.length){
			this.nowPlayingIndex = 0;
		}
		this.play();
	}
	
	renderInElement(list: HTMLElement){
		list.innerHTML = "";
		for(var i=0; i < this.songs.length; i++){
			list.innerHTML += this.songs[i].toHTML();
		}
	}
}