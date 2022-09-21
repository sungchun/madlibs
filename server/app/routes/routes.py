from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.Adjective import Adjective
from app.models.Adverb import Adverb
from app.models.Noun import Noun
from app.models.Verb import Verb
from app.models.WordSchema import word_schema, words_schema

api = Blueprint("api", __name__)

@api.route("/adjective", methods=["GET"])
def get_adjectives():
    all_adjectives = Adjective.query.all()
    result = words_schema.dump(all_adjectives)
    return jsonify(result)

@api.route("/adjective/<id>", methods=["GET"])
def get_adjective(id):
    adjective = Adjective.query.get(id)
    return word_schema.jsonify(adjective)

@api.route("/adjective", methods=["POST"])
def add_adjective():
    new_word = request.json["word"]
    new_adjective = Adjective(word = new_word)
    db.session.add(new_adjective)
    db.session.commit()
    return word_schema.jsonify(new_adjective)

@api.route("/adjective/<id>", methods=["POST"])
def update_adjective(id):
    adjective = Adjective.query.get(id)
    new_word = request.json["word"]
    adjective.word = new_word
    db.session.commit()
    return word_schema.jsonify(adjective)

@api.route("/adjective/<id>", methods=["DELETE"])
def delete_adjective(id):
    adjective = Adjective.query.get(id)
    db.session.delete(adjective)
    db.session.commit()
    return word_schema.jsonify(adjective)


@api.route("/adverb", methods=["GET"])
def get_adverbs():
    all_adverbs = Adverb.query.all()
    result = words_schema.dump(all_adverbs)
    return jsonify(result)

@api.route("/adverb/<id>", methods=["GET"])
def get_adverb(id):
    adverb= Adverb.query.get(id)
    return word_schema.jsonify(adverb)

@api.route("/adverb", methods=["POST"])
def add_adverb():
    new_word = request.json["word"]
    new_adverb= Adverb(word = new_word)
    db.session.add(new_adverb)
    db.session.commit()
    return word_schema.jsonify(new_adverb)

@api.route("/adverb/<id>", methods=["POST"])
def update_adverb(id):
    adverb = Adverb.query.get(id)
    new_word = request.json["word"]
    adverb.word = new_word
    db.session.commit()
    return word_schema.jsonify(adverb)

@api.route("/adverb/<id>", methods=["DELETE"])
def delete_adverb(id):
    adverb = Adverb.query.get(id)
    db.session.delete(adverb)
    db.session.commit()
    return word_schema.jsonify(adverb)


@api.route("/noun", methods=["GET"])
def get_nouns():
    all_nouns = Noun.query.all()
    result = words_schema.dump(all_nouns)
    return jsonify(result)

@api.route("/noun/<id>", methods=["GET"])
def get_noun(id):
    noun = Noun.query.get(id)
    return word_schema.jsonify(noun)

@api.route("/noun", methods=["POST"])
def add_noun():
    new_word = request.json["word"]
    new_noun = Noun(word = new_word)
    db.session.add(new_noun)
    db.session.commit()
    return word_schema.jsonify(new_noun)

@api.route("/noun/<id>", methods=["POST"])
def update_noun(id):
    noun = Noun.query.get(id)
    new_word = request.json["word"]
    noun.word = new_word
    db.session.commit()
    return word_schema.jsonify(noun)

@api.route("/noun/<id>", methods=["DELETE"])
def delete_noun(id):
    noun = Noun.query.get(id)
    db.session.delete(noun)
    db.session.commit()
    return word_schema.jsonify(noun)

@api.route("/verb", methods=["GET"])
def get_verbs():
    all_verbs = Verb.query.all()
    result = words_schema.dump(all_verbs)
    return jsonify(result)

@api.route("/verb/<id>", methods=["GET"])
def get_verb(id):
    verb = Verb.query.get(id)
    return word_schema.jsonify(verb)

@api.route("/verb", methods=["POST"])
def add_verb():
    new_word = request.json["word"]
    new_verb = Verb(word = new_word)
    db.session.add(new_verb)
    db.session.commit()
    return word_schema.jsonify(new_verb)

@api.route("/verb/<id>", methods=["POST"])
def update_verb(id):
    verb = Verb.query.get(id)
    new_word = request.json["word"]
    verb.word = new_word
    db.session.commit()
    return word_schema.jsonify(verb)

@api.route("/verb/<id>", methods=["DELETE"])
def delete_verb(id):
    verb = Verb.query.get(id)
    db.session.delete(verb)
    db.session.commit()
    return word_schema.jsonify(verb)

