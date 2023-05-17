from flask import request,flash
import re


def check_password(password1,password2):
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
        flash('Konto zostało założone', category='success')
