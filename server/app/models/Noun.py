from app.extensions import db

class Noun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Noun {self.word}'
