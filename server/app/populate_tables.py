import app
from app.extensions import db
from app.models import Adjective, Adverb, Noun, Verb
import csv

def populate_adjectives():
    with open("/home/projuser/src/app/words/adjectives.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adjective.Adjective(word=row)
            db.session.add(new)
        db.session.commit()

def populate_adverbs():
    with open("/home/projuser/src/app/words/adverbs.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adverb.Adverb(word=row)
            db.session.add(new)
        db.session.commit()

def populate_nouns():
    with open("/home/projuser/src/app/words/nouns.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Noun.Noun(word=row)
            db.session.add(new)
        db.session.commit()

def populate_verbs():
    with open("/home/projuser/src/app/words/verbs.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Verb.Verb(word=row)
            db.session.add(new)
        db.session.commit()

def main():
    populate_adjectives()
    populate_adverbs()
    populate_nouns()
    populate_verbs()

if __name__ == "__main__":
    main()
