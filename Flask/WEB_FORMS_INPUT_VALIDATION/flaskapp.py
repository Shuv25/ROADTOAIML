from flask import Flask,render_template,url_for,redirect,flash
from forms import SignupForm,LoginForm

app=Flask(__name__)
app.config["SECRET_KEY"]="gagan_chutiya"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="Home")

@app.route('/signup',methods=["GET","POST"])
def signup():
    form=SignupForm()

    if form.validate_on_submit():
        flash(f"Succefully Regusterd {form.username.data}")
        return redirect(url_for("home"))
    
    return render_template('signup.html',title="SignUp",form=form)

@app.route('/login',methods=["GET","POST"])
def login():
    form=LoginForm()
    email=form.email.data
    password=form.password.data

    if form.validate_on_submit():
        if email=="shuvsutradhar@gmail.com" and password=="zxcvb":
            flash(f"Logged In Succefully")
            return redirect(url_for("home"))
        else:
            flash ("Incorrect email or password")
    return render_template('login.html',title="LogIn",form=form)

if __name__=='__main__':
    app.run(debug=True)