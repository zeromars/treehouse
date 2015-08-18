/*(function(){
function foo(){
	console.log('foobar');
};

foo();

}());*/

// + and ! are good for concatinating files together
// + expression to be evaulated
// http://stackoverflow.com/questions/3755606/what-does-the-exclamation-mark-do-before-the-function
// https://github.com/airbnb/javascript/issues/44#issuecomment-13063933

+function(){
function foo(){
	console.log('foobar');
};

foo();

}();

!function(){
function foo2(){
	console.log('foobar2');
};

foo2();

}();

//exports

var awesomeNewModule = (function(){
	var exports = {
		foo: 5,
		bar: 10
	};
	exports.HelloMars = function(){
		console.log('Hello Mars');
	};
	exports.goodbye = function(){
		console.log('Goodbye');
	};
	return exports;
}());

//loose augmentation

var awesomeNewModule = (function(exports){
	var exports = {
		foo: 5,
		bar: 10
	};
	exports.HelloMars = function(){
		console.log('Hello Mars');
	};
	exports.goodbye = function(){
		console.log('Goodbye');
	};
	return exports;
}(awesomeNewModule || {}));

//sub module pattern

var awesomeNewModule.sub = (function(exports){
	var exports = {
		foo: 5,
		bar: 10
	};
	exports.HelloMars = function(){
		console.log('Hello Mars');
	};
	exports.goodbye = function(){
		console.log('Goodbye');
	};
	return exports;
}(awesomeNewModule.sub || {}));

/*
if (typeof module !== 'undefined' && module.exports) {
	module.exports = Polyglot;
}else{
	root.Polyglot = Polyglot;
}
*/