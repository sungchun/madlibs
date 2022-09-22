from extensions import db
from models import Adjective, Adverb, Noun, Verb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

engine = create_engine('postgresql://madlibs_dev:madlibs_dev@db/madlibs_dev')

Session = sessionmaker()
local_session = Session(bind=engine)

def populate_adjectives():
    with open("/home/projuser/src/app/words/adjectives.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adjective.Adjective(word=row)
            local_session.add(new)

        local_session.commit()

def populate_adverbs():
    with open("/home/projuser/src/app/words/adverbs.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Adverb.Adverb(word=row)
            local_session.add(new)

        local_session.commit()

def populate_nouns():
    with open("/home/projuser/src/app/words/nouns.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Noun.Noun(word=row)
            local_session.add(new)

        local_session.commit()

def populate_verbs():
    with open("/home/projuser/src/app/words/verbs.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            new = Verb.Verb(word=row)
            local_session.add(new)

        local_session.commit()

def main():
    populate_adjectives()
    populate_adverbs()
    populate_nouns()
    populate_verbs()

if __name__ == "__main__":
    main()
