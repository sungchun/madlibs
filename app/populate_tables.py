from __init__ import db, Adjective, Adverb, Noun, Verb
import csv

def populate_adjectives():
    with open("words/adjectives.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adjective(word=row)
            db.session.add(new)
        db.session.commit()

def populate_adverbs():
    with open("words/adverbs.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adverb(word=row)
            db.session.add(new)
        db.session.commit()

def populate_nouns():
    with open("words/nouns.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Noun(word=row)
            db.session.add(new)
        db.session.commit()

def population_verbs():
    with open("words/verbs.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Verb(word=row)
            db.session.add(new)
        db.session.commit()

def main():
    populate_adjectives()
    populate_adverbs()
    populate_nouns()
    populate_verbs()

if __name__ == "__main__":
    main()
