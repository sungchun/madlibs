from app.extensions import ma

class WordSchema(ma.Schema):
    class Meta:
        fields = ('id', 'word')

word_schema = WordSchema()
words_schema = WordSchema(many=True)

