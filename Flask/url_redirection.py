from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/home/<name>')
def home(name):
    return f"<h3>Hi {name.title()}, welocme to home page</h3>"

@app.route('/pass')
def passed():
    return "Congratz, you have passed the exam"

@app.route('/fail')
def failed():
    return "Sorry, you haven't passed the exam"

@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num>=30:
        return redirect(url_for('passed'))
    else:
        return redirect(url_for('failed'))

if __name__=='__main__':
    app.run(debug=1)