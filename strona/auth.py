from flask import Blueprint, render_template, request
from .funkcje import check_password
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text = "Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        second_name = request.form.get('secondName')
        company_name = request.form.get('nazwaFirmy')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        check_password(password1,password2)

    return render_template("sign_up.html")