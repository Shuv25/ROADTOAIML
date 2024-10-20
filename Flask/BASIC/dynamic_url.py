from flask import Flask

app=Flask(__name__)


@app.route('/')
@app.route('/home/<name>')
def home(name):
    return f"<h3>Hi {name.title()},welcome to this page</h3"

if __name__=='__main__':
    app.run(debug=True)