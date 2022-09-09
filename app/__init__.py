import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:banana@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Adjective(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Adjective {self.word}>'

class Adverb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Adjective {self.word}>'

class Noun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Adjective {self.word}>'

class Verb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Adjective {self.word}>'

class WordSchema(ma.Schema):
    class Meta:
        fields = ('id', 'word')

word_schema = WordSchema()
words_schema = WordSchema(many=True)

@app.route("/adjective", methods=["GET"])
def get_adjectives():
    all_adjectives = Adjective.query.all()
    result = words_schema.dump(all_adjectives)
    return jsonify(result)

@app.route("/adjective/<id>", methods=["GET"])
def get_adjective(id):
    adjective = Adjective.query.get(id)
    return word_schema.jsonify(adjective)

@app.route("/adjective", methods=["POST"])
def add_adjective():
    new_word = request.json["word"]
    new_adjective = Adjective(word = new_word)
    db.session.add(new_adjective)
    db.session.commit()
    return word_schema.jsonify(new_adjective)

@app.route("/adjective/<id>", methods=["POST"])
def update_adjective(id):
    adjective = Adjective.query.get(id)
    new_word = request.json["word"]
    adjective.word = new_word
    db.session.commit()
    return word_schema.jsonify(adjective)

@app.route("/adjective/<id>", methods=["DELETE"])
def delete_adjective(id):
    adjective = Adjective.query.get(id)
    db.session.delete(adjective)
    db.session.commit()
    return word_schema.jsonify(adjective)


@app.route("/adverb", methods=["GET"])
def get_adverbs():
    all_adverbs = Adverb.query.all()
    result = words_schema.dump(all_adverbs)
    return jsonify(result)

@app.route("/adverb/<id>", methods=["GET"])
def get_adverb(id):
    adverb= Adverb.query.get(id)
    return word_schema.jsonify(adverb)

@app.route("/adverb", methods=["POST"])
def add_adverb():
    new_word = request.json["word"]
    new_adverb= Adverb(word = new_word)
    db.session.add(new_adverb)
    db.session.commit()
    return word_schema.jsonify(new_adverb)

@app.route("/adverb/<id>", methods=["POST"])
def update_adverb(id):
    adverb = Adverb.query.get(id)
    new_word = request.json["word"]
    adverb.word = new_word
    db.session.commit()
    return word_schema.jsonify(adverb)

@app.route("/adverb/<id>", methods=["DELETE"])
def delete_adverb(id):
    adverb = Adverb.query.get(id)
    db.session.delete(adverb)
    db.session.commit()
    return word_schema.jsonify(adverb)


@app.route("/noun", methods=["GET"])
def get_nouns():
    all_nouns = Noun.query.all()
    result = words_schema.dump(all_nouns)
    return jsonify(result)

@app.route("/noun/<id>", methods=["GET"])
def get_noun(id):
    noun = Noun.query.get(id)
    return word_schema.jsonify(noun)

@app.route("/noun", methods=["POST"])
def add_noun():
    new_word = request.json["word"]
    new_noun = Noun(word = new_word)
    db.session.add(new_noun)
    db.session.commit()
    return word_schema.jsonify(new_noun)

@app.route("/noun/<id>", methods=["POST"])
def update_noun(id):
    noun = Noun.query.get(id)
    new_word = request.json["word"]
    noun.word = new_word
    db.session.commit()
    return word_schema.jsonify(noun)

@app.route("/noun/<id>", methods=["DELETE"])
def delete_noun(id):
    noun = Noun.query.get(id)
    db.session.delete(noun)
    db.session.commit()
    return word_schema.jsonify(noun)

@app.route("/verb", methods=["GET"])
def get_verbs():
    all_verbs = Verb.query.all()
    result = words_schema.dump(all_verbs)
    return jsonify(result)

@app.route("/verb/<id>", methods=["GET"])
def get_verb(id):
    verb = Verb.query.get(id)
    return word_schema.jsonify(verb)

@app.route("/verb", methods=["POST"])
def add_verb():
    new_word = request.json["word"]
    new_verb = Verb(word = new_word)
    db.session.add(new_verb)
    db.session.commit()
    return word_schema.jsonify(new_verb)

@app.route("/verb/<id>", methods=["POST"])
def update_verb(id):
    verb = Verb.query.get(id)
    new_word = request.json["word"]
    verb.word = new_word
    db.session.commit()
    return word_schema.jsonify(verb)

@app.route("/verb/<id>", methods=["DELETE"])
def delete_verb(id):
    verb = Verb.query.get(id)
    db.session.delete(verb)
    db.session.commit()
    return word_schema.jsonify(verb)
