import re

from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import db
from .models import User
from .walidacja import check_password
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required,logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Zalogowano!',category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Złe hasło, spróbuj pownownie',category='error')
        else:
            flash('Email nie jest przypisany do zadnego konta')

    return render_template("login.html", text = "Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/adek')
def adek():
    return render_template("adek.html", text = "Testing")

@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        second_name = request.form.get('secondName')
        company_name = request.form.get('nazwaFirmy')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email jest zajęty :(((((.', category='error')
        if not password1 == password2:
            flash('Hasła muszą być identyczne', category="error")

        if not re.search(r'\d', password1):
            flash('Hasło musi mieć min. 1 cyfrę', category="error")

        if not re.search(r'[A-Z]', password1):
            flash('Hasło musi mieć min. 1 wielką literę', category="error")

        if not re.search(r'[!@#$%^&*()_+=-]', password1):
            flash('Hasło musi mieć min. 1 znak specjalny', category="error")

        elif len(password1) < 8 or len(password1) > 32:
            flash('Hasło musi mieć min. 8 znaków i max 32 znaków', category="error")
        else:
            new_user = User(email=email, first_name=first_name, second_name = second_name,password= generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Konto zostało założone', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")