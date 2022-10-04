# from ..extensions import db

# from sqlalchemy.dialects.mysql import ENUM

# class Team(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     teamname = db.Column(db.String(200), nullable=False)
#     filled = db.Column(db.Boolean, unique=False, default=True)
    
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
#     project = db.relationship('Project', backref=db.backref('project_team'))

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', backref=db.backref('user_team'))    
   
#     join_id = db.Column(db.Integer, db.ForeignKey('join_request.id', ondelete='CASCADE'), nullable=False)
#     join_requests = db.relationship('JoinRequest', backref=db.backref('join_request_team'))
    
# class TeamAbout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     description = db.Column(db.String(50))

#     team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
#     team = db.relationship('Team', backref=db.backref('team_about'))

# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     projectname = db.Column(db.String(50))
#     url = db.Column(db.String(200))

#     team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
#     team = db.relationship('Team', backref=db.backref('team_project'))

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', backref=db.backref('user_project')) 

# class ProjectAbout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_name = db.Column(db.String(50))
#     description = db.Column(db.String(50))

#     project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
#     project = db.relationship('Team', backref=db.backref('project_about'))

# class JoinRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
    
#     team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
#     team = db.relationship('Team', backref=db.backref('team_join_request'))

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', backref=db.backref('user_join_request')) 

#     status = db.Column(ENUM('pending', 'denied', 'accepted', 'withdrawn'))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# class UserAbout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(50))
#     bio =  db.Column(db.Text(), nullable=False)
#     joined_date = db.Column(db.DateTime(), nullable=False)
#     last_accessed = db.Column(db.DateTime())
    
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', backref=db.backref('user_about'))
    
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=True)
#     project = db.relationship('Project', backref=db.backref('user_about'))
    
#     team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=True)
#     team = db.relationship('Team', backref=db.backref('user_about'))