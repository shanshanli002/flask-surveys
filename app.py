from crypt import methods
from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *
app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "never-tell!"
toolbar = DebugToolbarExtension(app)

satisfaction_answers = []
personality_answers = []

@app.route('/')
def survey_welcome():
    """welcome user to take survey"""
    return render_template('welcome.html')

@app.route("/question/<int:q>")
def reveal_question(q):
    satisfaction_q = len(satisfaction_answers)
    personality_q = len(personality_answers)
    if satisfaction_q <= 4:
        user_question = surveys['satisfaction'].questions[satisfaction_q].question
        question_options = surveys['satisfaction'].questions[satisfaction_q].choices
    
    
        
    return render_template('question.html', user_question=user_question, question_options=question_options)
    
    
@app.route('/answer', methods=["POST"])
def store_answer():
    user_answer = request.form['user_answer']
    if len(satisfaction_answers) < 4:
        satisfaction_answers.append(user_answer)
        q = len(satisfaction_answers)+1
        return redirect(f'/question/{q}')
