from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "welcome to home"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h3>Hi {name.title()}, you are welocme to this page.</h3>"

@app.route('/addition/<int:num>')
def add(num):
    return f"<h3>Input is {num}, addition is {num+5}.</h3>"

@app.route('/additiontwo/<int:num>/<int:numsec>')
def addtwo(num,numsec):
    return f"<h3>Input is {num,numsec}, addition is {num+numsec}.</h3>"

@app.route('/about')
def about():
    return "welcome to about page"

if __name__=="__main__":
    app.run(debug=True)

 


