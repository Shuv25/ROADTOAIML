from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/home/<name>')
def home(name):
    return f"<h3>Hi {name.title()}, welocme to home page</h3>"

@app.route('/pass/<sname>/<int:score>')
def passed(sname,score):
    return f"Congratz, {sname.title()} you have passed the exam with {score} score"

@app.route('/fail/<sname>/<int:score>')
def failed(sname,score):
    return f"Sorry, {sname.title()} your mark {score} doesn't exceed the passing mark 30"

@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num>=30:
        return redirect(url_for('passed',sname=name,score=num))
    else:
        return redirect(url_for('failed',sname=name,score=num))

if __name__=='__main__':
    app.run(debug=1)