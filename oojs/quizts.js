/// <reference path="questions.ts" />
var Question = (function () {
    function Question(question, type, points, choices, answer) {
        this.question = question;
        this.type = type;
        this.points = points;
        this.choices = choices;
        this.answer = answer;
    }
    return Question;
})();
var Quiz = (function () {
    function Quiz() {
        this.maxpoints = 43;
        this.totalpoints = 0;
        this.questions = [];
        this.currentQuestion = 1;
    }
    Quiz.prototype.updateQuestion = function (num) {
        document.getElementById("question").innerHTML = questionList[(num - 1)].question;
    };
    Quiz.prototype.updateChoices = function (num) {
        var type = questionList[(num - 1)].type;
        var choice1 = document.getElementById("choice0");
        choice1.innerHTML = questionList[(num - 1)].choices[0].toString();
        var choice2 = document.getElementById("choice1");
        choice2.innerHTML = questionList[(num - 1)].choices[1].toString();
    };
    Quiz.prototype.updateProgress = function (num) {
        var html = 'Question ' + ((num === 0) ? 1 : num) + ' of ' + questionList.length;
        document.getElementById("progress").innerHTML = html;
    };
    Quiz.prototype.updatePoints = function (total) {
        this.totalpoints += total;
    };
    Quiz.prototype.add = function (question) {
        this.questions.push(question);
    };
    Quiz.prototype.question = function () {
        return this.questions[this.currentQuestion].question;
    };
    Quiz.prototype.answer = function () {
        return this.questions[this.currentQuestion].answer;
    };
    Quiz.prototype.questionType = function () {
        return this.questions[this.currentQuestion].type;
    };
    Quiz.prototype.check = function (question, num) {
        if (questionList[(question - 1)].answer == questionList[num].answer) {
            this.updatePoints(questionList[(question - 1)].points);
        }
    };
    Quiz.prototype.events = function (num) {
        this.check(this.currentQuestion, num);
        this.currentQuestion += 1;
        if ((this.currentQuestion - 1) < questionList.length) {
            this.updateQuestion(this.currentQuestion);
            this.updateChoices(this.currentQuestion);
            this.updateProgress(this.currentQuestion);
        }
        else {
            var quizz = document.getElementById("quiz");
            quizz.innerHTML = '<h2>Game Over</h2><h3>You got ' + this.totalpoints + ' points out of ' + this.maxpoints + '!!</h3>';
        }
    };
    Quiz.prototype.setup = function () {
        for (var i = 0; i <= questionList.length; i++) {
            this.add(questionList[i]);
        }
        var self = this;
        this.updateQuestion(this.currentQuestion);
        this.updateChoices(this.currentQuestion);
        this.updateProgress(this.currentQuestion);
        var guess0 = document.getElementById("guess0");
        var guess1 = document.getElementById("guess1");
        guess0.onclick = function () {
            self.events(0);
        };
        guess1.onclick = function () {
            self.events(1);
        };
        return this.question;
    };
    return Quiz;
})();
var quiz = new Quiz();
quiz.setup();
