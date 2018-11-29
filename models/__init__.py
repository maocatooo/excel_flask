from mongoengine import *

connect('test', host='mongo', port=27017)  # mongo is system Hosts file


class User(Document):
    meta = {"collection": "user"}
    username = StringField()
    pwd = StringField()

    def __str__(self):
        return "<class {0} {1}>".format(self.__class__.__name__, self.username.encode('utf-8'))

    __repr__ = __str__

