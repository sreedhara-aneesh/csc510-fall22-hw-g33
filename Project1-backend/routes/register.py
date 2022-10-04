from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ..extensions import db
from ..models.all import User
# from ..models.user import User
# from ..models.team import Team
# from ..models.project import Project

import functools
from werkzeug.security import check_password_hash, generate_password_hash

registerer = Blueprint('auth', __name__, url_prefix='/auth')
@registerer.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                user = User((username, generate_password_hash(password)))
                db.session.add(user)
                db.session.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                # return http error 
                return redirect(url_for("auth.login"))
        flash(error)
    return {"success":"200"}