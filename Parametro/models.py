from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, LazyReferenceField, DynamicDocument
from PropHorizontal.models import Propiedades_Horizontales

class Parametros(DynamicDocument):
    PROPIEDAD_ID = fields.LazyReferenceField(Propiedades_Horizontales, passthrough=False, dbref=False)
    TIPO = fields.StringField(required=True)