
try:

    from mongoengine import connect, Document, StringField
except ImportError:
    def connect(*args, **kwargs):
        pass

    class Document(object):

        def save(self):
            pass


    class StringField(object):
        pass


connect('test', host='mongo', port=27017)  # mongo is system Hosts file


class User(Document):
    meta = {"collection": "user"}
    username = StringField()
    pwd = StringField()

