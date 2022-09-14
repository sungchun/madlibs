from flask_marshmallow import Marshmallow

class WordSchema(ma.Schema):
    class Meta:
        fields = ('id', 'word')

word_schema = WordSchema()
words_schema = WordSchema(many=True)
