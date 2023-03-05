from flask import Flask,render_template,request,session,logging,url_for,redirect,flash,g,send_from_directory,send_file
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=['GET','POST'])
def startChat():
    if request.method == 'POST':
        session['firstname'] = request.form['firstName']
        session['lastname'] = request.form['lastName']
        session['email'] = request.form['userMail']
        return render_template('home.html')
    return render_template("signup.html")

@app.route("/endchatbox",methods=['GET','POST'])
def end():
    return render_template('end.html',firstname=session.get('firstname'),lastname=session.get('lastname'),email=session.get('email'))

def chatbot_response(message):
    question_dict = {"Does the college have a football team?":"Yes the college has a football team named Cincinnati Bearcats football",
    "Does the college have a football team":"Yes the college has a football team named Cincinnati Bearcats football",
    "Does it have Computer Science Major?":"Yes University of Cincinnati offers a computer science major",
    "Does it have Computer Science Major":"Yes University of Cincinnati offers a computer science major",
    "What is the in-state tuition?":"The in-state tution for University of Cincinnati is 12,598 USD",
    "What is the in-state tuition":"The in-state tution for University of Cincinnati is 12,598 USD",
    "Does its have on campus housing?":"Yes University of Cincinnati provides on campus housing",
    "Does its have on campus housing":"Yes University of Cincinnati provides on campus housing" }
    msg = message.strip()
    if msg in question_dict:
        return question_dict[msg]
    else:
        return "Please ask a valid Question"

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)

if __name__== "__main__":
    app.run(debug=True)