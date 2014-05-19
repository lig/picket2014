from mongoengine.document import Document
from mongoengine.fields import SequenceField, StringField, ListField


class Issue(Document):
    id = SequenceField()
    subject = StringField(required=True)
    comments = ListField(StringField())
