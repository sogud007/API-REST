from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class Modulos(Document):
    NOMBRE = fields.StringField(required=True)
    DEPENDENCIAS = fields.ListField(fields.StringField(required=True))