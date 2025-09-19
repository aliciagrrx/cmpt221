"""professor.py: create a table named professors in the marist database"""
from db.server import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, first_name, last_name, email):
       self.FirstName = first_name
       self.LastName = last_name
       self.Email = email

    def __repr__(self):
        return f"<Professor {self.ProfessorID}: {self.FirstName} {self.LastName}, Email={self.Email}>"
    
    def __repr__(self):
        return self.__repr__()