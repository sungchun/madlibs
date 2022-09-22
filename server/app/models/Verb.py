from app.extensions import db

class Verb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)
    schema = 'WordSchema'

    def __repr__(self):
        return f'Verb {self.word}'
