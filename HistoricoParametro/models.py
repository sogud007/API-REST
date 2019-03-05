from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, ReferenceField, DynamicDocument
from Usuario.models import Usuarios
import datetime

class Historico_Parametros(DynamicDocument):
    PROPIEDAD_ID = fields.ReferenceField(Usuarios)
    TIPO = fields.StringField(required=True)
    FECHA_DESDE = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_HASTA = fields.DateTimeField(default=datetime.datetime.utcnow)