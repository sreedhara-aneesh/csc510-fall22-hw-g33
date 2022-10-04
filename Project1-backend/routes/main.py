from flask import Blueprint

from ..extensions import db
from ..models.user import User
from ..models.team import Team
from ..models.project import Project

main = Blueprint('main', __name__)

@main.route('/user/<name>')
def create_user(name):
    user = User(name=name, password="12345",email="jnj@gmaj.vom")
    db.session.add(user)
    db.session.commit()

    return 'Created User!'