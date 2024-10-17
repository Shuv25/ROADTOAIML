from flask import Flask,render_template,url_for
from employee import employes

app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="Home")#place holders and parameters

@app.route('/about')
def about():
    return render_template('about.html',title="About")

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html',title="Evaluate",number=num)

@app.route('/employees')
def employees():
    return render_template('employees.html',title="Empoyees",employee_data=employes)

@app.route('/employees/manager')
def manager():
    return render_template('manager.html',title="Managers",employee_data=employes)

if __name__=='__main__':
    app.run(debug=True)