from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, DynamicDocument, LazyReferenceField
from PropHorizontal.models import Propiedades_Horizontales
import datetime

class Noticias(DynamicDocument):
    PROPIEDAD_ID = fields.LazyReferenceField(Propiedades_Horizontales, passthrough=False, dbref=False)
    TITULO = fields.StringField(required=True)
    MENSAJE = fields.StringField(required=True)
    IMAGEN = fields.FileField()
    TIPO = fields.StringField(required=True)
    FECHA_INICIO = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_FIN = fields.DateTimeField(default=datetime.datetime.utcnow)
    HABILITADO = fields.BooleanField()