from ..extensions import db

from sqlalchemy.dialects.mysql import ENUM

class Joinrequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    team = db.relationship('Team', backref=db.backref('team_joinrequest'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_joinrequest')) 

    status = db.Column(ENUM('pending', 'denied', 'accepted', 'withdrawn'))