/// <reference path="questions.ts" />
class Question {
	constructor(
		public question:string,
		public type:string,
		public points:number,
		public choices:Object,
		public answer:number) {		
	}	
}

class Quiz {
	questions: Question[];
	currentQuestion:number;
	maxpoints:number = 43;
	totalpoints:number =0;
	
	constructor() {
		this.questions = [];
		this.currentQuestion = 1;		
	}	
	
	updateQuestion(num){
		document.getElementById("question").innerHTML = questionList[(num-1)].question;
	}
	
	updateChoices(num){
		var type = questionList[(num-1)].type;
		var choice1 = document.getElementById("choice0"); 		
		choice1.innerHTML = questionList[(num-1)].choices[0].toString();
		var choice2 = document.getElementById("choice1"); 
		choice2.innerHTML = questionList[(num-1)].choices[1].toString();
	}
	
	updateProgress(num){
		var html = 'Question '+((num===0) ? 1: num)+' of ' + questionList.length;
		document.getElementById("progress").innerHTML = html;
	}
	
	updatePoints(total){
		this.totalpoints += total;
	}
	
	add(question){
		this.questions.push(question);
	}
	
	question(){
		return this.questions[this.currentQuestion].question;
	}
	
	answer(){
		return this.questions[this.currentQuestion].answer;
	}
	
	questionType(){
		return this.questions[this.currentQuestion].type;
	}
	
	check(question, num){
		if(questionList[(question-1)].answer == questionList[num].answer){
			this.updatePoints(questionList[(question-1)].points);
		}
	}
	
	events(num){
		this.check(this.currentQuestion, num);
		this.currentQuestion+=1;
		if((this.currentQuestion - 1) < questionList.length){
			this.updateQuestion(this.currentQuestion);
			this.updateChoices(this.currentQuestion);
			this.updateProgress(this.currentQuestion);
		}else{
			var quizz = document.getElementById("quiz");
			quizz.innerHTML = '<h2>Game Over</h2><h3>You got '+this.totalpoints+' points out of '+this.maxpoints+'!!</h3>';
		}
	}
	
	setup(){
		for (var i=0;i<= questionList.length; i++){
			this.add(questionList[i]);
		}
		var self = this;
		
		this.updateQuestion(this.currentQuestion);
		this.updateChoices(this.currentQuestion);
		this.updateProgress(this.currentQuestion);
		var guess0 = document.getElementById("guess0");
		var guess1 = document.getElementById("guess1");
		guess0.onclick = function(){
			self.events(0);
		};
		guess1.onclick = function(){
			self.events(1);
		};
		return this.question;
	}
}

var quiz = new Quiz();

quiz.setup();