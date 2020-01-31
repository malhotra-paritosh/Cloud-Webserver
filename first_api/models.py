from first_api import db

class Dummy_users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __repr_(self):
        return f"User('{self.userName}', '{self.email}' )"
