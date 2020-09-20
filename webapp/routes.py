from webapp import app, db
from flask import render_template, request, redirect, url_for
from webapp.forms import RegistrationForm, LoginForm, AddFeedForm
from webapp.models import User, Feed, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user

# Home route / landing/ welcome page
@app.route('/')
def home():
    return render_template("home.html")

# Register route / view / page where new users register
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username, email, password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

# Logging out route / button for users to log out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

# Loggin out route / view / page for user to log in

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            return render_template('myaccount.html')
        else:
            return "Something went wrong. Please check your info an try again."
    return render_template('login.html', form=form)

# My Account view where users add their feeds (MVP of "my feeds / feeds  I'm subscribed to")

@app.route('/addfeed', methods=['GET', 'POST'])
def addfeed():
    feed = AddFeedForm()
    if request.method == 'POST' and feed.validate():
        link = feed.link.data

        f = Feed(link)

        db.session.add(f)
        db.session.commit()
        return render_template('myaccount.html', feed=feed)
    return render_template('myaccount.html')