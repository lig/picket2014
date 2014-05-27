from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import (SequenceField, StringField, ListField,
    ReferenceField, DateTimeField)

from users.documents import User


class Issue(Document):
    meta = {
        'ordering': ['-id']
    }

    id = SequenceField(primary_key=True)
    subject = StringField(required=True)
    creator = ReferenceField(User)
    comments = ListField(StringField())
    created = DateTimeField(default=lambda: datetime.utcnow())
    modified = DateTimeField(default=lambda: datetime.utcnow())

    def __str__(self):
        return '#{}: {}'.format(self.id, self.subject)

    def save(self, *args, **kwargs):
        self.modified = datetime.utcnow()
        return Document.save(self, *args, **kwargs)