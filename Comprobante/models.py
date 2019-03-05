from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, ReferenceField, DynamicDocument
import datetime
from PropHorizontal.models import Propiedades_Horizontales

class UnidadPrivadaField(EmbeddedDocument):
    IDENTIFICADOR = fields.StringField(required=True)
    GRUPO = fields.StringField(required=True)
    UNIDAD_PRIVADA_ID = fields.ReferenceField('Unidades_Privadas')

class Comprobantes(Document):
    PROPIEDAD_ID = fields.ReferenceField(Propiedades_Horizontales)
    UNIDAD_PRIVADA = fields.EmbeddedDocumentField(UnidadPrivadaField)
    PERIODO = fields.StringField(required=True)
    VALOR = fields.IntField()
    DOCUMENTO = fields.FileField()
    FECHA_PAGO = fields.DateTimeField(default=datetime.datetime.utcnow)

