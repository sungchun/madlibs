import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:banana@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

@app.route("/adjective", methods=["GET"])
def get_adjectives():
    result = Adjective.Query.all()
    return jsonify(result.data)

@app.route("/adjective/<id>", methods=["GET"])
def get_adjective(id):
    adjective = Adjective.query.get(id)
    return jsonify(adjective)

@app.route("/adjective", methods=["POST"])
def add_adjective():
    new_word = request.json["word"]
    new_adjective = Adjective(word = new_word)
    db.session.add(new_adjective)
    db.session.commit()
    return jsonify(new_adjective)

@app.route("/adjective/<id>", methods=["POST"])
def adjective_update(id):
    adjective = Adjective.query.get(id)
    new_word = request.json["word"]
    adjective.word = new_word
    db.session.commit()
    return jsonify(adjective)

@app.route("/adjective/<id>", methods=["DELETE"])
def adjective_delete(id):
    adjective = Adjective.query.get(id)
    db.session.delete(adjective)
    db.session.commit()
    return jsonify(adjective)


