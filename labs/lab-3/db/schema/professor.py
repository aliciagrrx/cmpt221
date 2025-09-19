"""professor.py: create a table named professors in the marist database"""
from db.server import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(120))

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, name):
       self.FirstName = self.FirstName
       self.LastName = self.LastName
       self.Email = self.Email

    def __repr__(self):
        return f"""
            "FIRST NAME: {self.FirstName}
            "LAST NAME: {self.LastName}
            "EMAIL: {self.Email}
        """
    def __repr__(self):
        return self.__repr__()