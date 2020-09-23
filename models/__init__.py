
try:

    from mongoengine import connect, Document, StringField
except ImportError:
    def connect(*args, **kwargs):
        pass

    class Document(object):

        def save(self):
            users.append(self)

        @property
        def objects(self):
            return type("A", (object,), {"all": lambda *args, **kwargs: users})

    class StringField(object):
        pass


connect('test', host='mongo', port=27017)  # mongo is system Hosts file

users = []


class User(Document):
    meta = {"collection": "user"}
    username = StringField()
    pwd = StringField()

