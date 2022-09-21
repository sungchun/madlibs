from app.extensions import db

class Adjective(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Adjective {self.word}>'
