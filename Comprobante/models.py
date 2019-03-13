from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, ReferenceField, DynamicDocument, LazyReferenceField
import datetime

class UnidadPrivadaField(EmbeddedDocument):
    IDENTIFICADOR = fields.StringField(required=True)
    GRUPO = fields.StringField(required=True)
    UNIDAD_PRIVADA_ID = fields.LazyReferenceField('Unidades_Privadas', passthrough=False, dbref=False)

class Comprobantes(Document):
    PROPIEDAD_ID = fields.LazyReferenceField('Propiedades_Horizontales', passthrough=False, dbref=False)
    UNIDAD_PRIVADA = fields.EmbeddedDocumentField(UnidadPrivadaField)
    PERIODO = fields.StringField(required=True)
    VALOR = fields.IntField()
    DOCUMENTO = fields.FileField()
    FECHA_PAGO = fields.DateTimeField(default=datetime.datetime.utcnow)

