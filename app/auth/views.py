from flask import render_template,redirect,url_for, request, flash
from flask.helpers import flash
from flask_wtf import form
from ..models import User
from .forms import SignUpForm, LoginForm
from .. import db, photos
from . import auth
from flask_login import login_user, logout_user, login_required
from ..email import mail_message

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        filename = photos.save(form.profile.data)
        profile_pic_path = f'img/{filename}'
        user = User(email = form.email.data, fname= form.fname.data, lname=form.lname.data, username = form.username.data, profile_pic_path=profile_pic_path, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to PitchPanel.","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))

    title = 'Sign Up | PitchPanel'
    return render_template('auth/signup.html', signup_form = form, title = title)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password.')

    title = 'Log In | PitchPanel'
    return render_template('auth/login.html', login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))