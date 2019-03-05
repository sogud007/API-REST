from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, ReferenceField, DynamicDocument
from PropHorizontal.models import Propiedades_Horizontales
import datetime

class Cobros(DynamicDocument):
    PROPIEDAD_ID = fields.ReferenceField(Propiedades_Horizontales)
    PERIODO = fields.StringField(required=True)
    TIPO = fields.StringField(required=True)
    DESCRIPCION = fields.StringField()
    VALOR = fields.IntField()
    FECHA = fields.DateTimeField(default=datetime.datetime.utcnow)
    HABILITADO = fields.BooleanField()