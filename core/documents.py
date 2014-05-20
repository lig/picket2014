from mongoengine.document import Document
from mongoengine.fields import SequenceField, StringField, ListField,\
    ReferenceField

from users.documents import User


class Issue(Document):
    meta = {
        'ordering': ['-id']
    }

    id = SequenceField(primary_key=True)
    subject = StringField(required=True)
    creator = ReferenceField(User)
    comments = ListField(StringField())

    def __str__(self):
        return '#{}: {}'.format(self.id, self.subject)
