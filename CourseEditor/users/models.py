from CourseEditor import db

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)

    def __init__(self, username, password, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True