from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, ReferenceField, DynamicDocument
from PropHorizontal.models import Propiedades_Horizontales

class Parametros(DynamicDocument):
    PROPIEDAD_ID = fields.ReferenceField(Propiedades_Horizontales)
    TIPO = fields.StringField(required=True)