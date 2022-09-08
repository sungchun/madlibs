from __init__ import db, Adjective, Adverb, Noun, Verb
import csv

def populate_adjectives():
    with open("words/adjectives.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adjective(word=row)
            db.session.add(new)
        db.session.commit()

populate_adjectives()

