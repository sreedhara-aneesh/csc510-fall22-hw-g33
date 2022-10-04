from ..extensions import db

from sqlalchemy.dialects.mysql import ENUM

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String(50))
    url = db.Column(db.String(200))

    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    team = db.relationship('Team', backref=db.backref('team_project'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_project')) 
