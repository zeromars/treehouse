var questions = [
	{
		question: 'How much do i love my babe?',
		type: 'ab',
		points: 5,
		choices: [
			'Infinity',
			'Bussel and a peck and a hug around the neck'
		],
		answer: 0
	},
	{
		question: 'How cute is koda?',
		type: 'ab',
		points: 4,
		choices: [
			'too cute',
			'Infinity'
		],
		answer: 1
	},
	{
		question: 'Is my babe a stinker?',
		type: 'ab',
		points: 3,
		choices: [
			'yes',
			'no'
		],
		answer: 1
	},
	{
		question: 'Is koda a stinker?',
		type: 'ab',
		points: 2,
		choices: [
			'yes',
			'no'
		],
		answer: 0
	},
	{
		question: 'How long can my babe keep me?',
		type: 'ab',
		points: 6,
		choices: [
			'day',
			'long as she can hold on'
		],
		answer: 1
	},
	{
		question: 'How many times did i fart making this?',
		type: 'ab',
		points: 1,
		choices: [
			0,
			'too many to count'
		],
		answer: 0
	},
];
var quiz = {
	currentQuestion: 1,
	totalpoints: 0,
	maxpoints: 21,
	update: {
		question: function(num){
			document.getElementById("question").innerHTML = questions[(num-1)].question;
		},
		choices: function(num){
			var type = questions[(num-1)].type;
			document.getElementById("choice0").innerHTML = questions[(num-1)].choices[0];
			document.getElementById("choice1").innerHTML = questions[(num-1)].choices[1];
		},
		progress: function(num){
			var html = 'Question '+((num===0) ? 1: num)+' of ' + questions.length;
			document.getElementById("progress").innerHTML = html;
		},
		points: function(total){
			quiz.totalpoints += total;
		}
	},
	check: {
		answer: function(question, num){
			if(questions[(question-1)].answer == questions[num].answer){
				quiz.update.points(questions[(question-1)].points);
			}
		}
	},
	events: {
		handleClick: function(num){
			quiz.check.answer(quiz.currentQuestion, num);
			quiz.currentQuestion+=1;
			if((quiz.currentQuestion - 1) < questions.length){
				quiz.update.question(quiz.currentQuestion);
				quiz.update.choices(quiz.currentQuestion);
				quiz.update.progress(quiz.currentQuestion);
			}else{
				var quizz = document.getElementById("quiz");
				quizz.innerHTML = '<h2>Game Over</h2><h3>You got '+quiz.totalpoints+' points out of '+quiz.maxpoints+'!!</h3>';
			}
		}
	},
	boot: function(){
		quiz.update.question(quiz.currentQuestion);
		quiz.update.choices(quiz.currentQuestion);
		quiz.update.progress(quiz.currentQuestion);
		var guess0 = document.getElementById("guess0");
		var guess1 = document.getElementById("guess1");
		guess0.onclick = function(){
			quiz.events.handleClick(0);
		};
		guess1.onclick = function(){
			quiz.events.handleClick(1);
		};
	}
};
quiz.boot();