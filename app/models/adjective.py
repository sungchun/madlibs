from app import db

class Adjective(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.string(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Adjective {self.word}>'
