from app imprt db

class Verb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.string(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Verb {self.word}'
