"""professor.py: create a table named professors in the marist database"""
from db.server import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    ProfessorFirstName = db.Column(db.String(40))
    ProfessorLastName =  db.Column(db.String(40))
    ProfessorEmailAddress = db.Column(db.String(40))

    CoreSubject = db.Column(db.String(40))
    YearsTeaching = db.column(db.Integer)
    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, Name, Year):
        self.ProfessorFirstName = self.ProfessorFirstName
        self.ProfessorLastName = self.ProfessorLastName
        self.ProfessorEmailAddress = self.ProfessorEmailAddress

    def __repr__(self):
        # add text to the f-string
        return f"""
            "ProfessorFirstName : {self.ProfessorName},
             ProfessorLastName : {self.ProfessorLastName},
             ProfessorEmailAddress : {self.ProfessorEmailAddress}
        """
    
    def __repr__(self):
        return self.__repr__()