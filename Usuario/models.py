from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, LazyReferenceField
#from UnidadPrivada.models import Unidades_Privadas
import datetime

class AsignacionPHField(EmbeddedDocument):
    ROL = fields.StringField(required=True)    
    FECHA_INICIO = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_FIN = fields.DateTimeField(default=datetime.datetime.utcnow)
    PROPIEDAD_ID = fields.LazyReferenceField('Propiedades_Horizontales', passthrough=False, dbref=False)
    HABILITADO = fields.BooleanField()

class UnidadPrivadaField(EmbeddedDocument):
    PROPIEDAD = fields.StringField(required=True)
    IDENTIFICADOR = fields.StringField(required=True)
    GRUPO = fields.StringField(required=True)
    UNIDAD_PRIVADA_ID = fields.LazyReferenceField('Unidades_Privadas', passthrough=False, dbref=False)
    PROPIEDAD_ID = fields.LazyReferenceField('Propiedades_Horizontales', passthrough=False, dbref=False)

class AsignacionUPField(EmbeddedDocument):
    ROL = fields.StringField(required=True)
    FECHA_INICIO = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_FIN = fields.DateTimeField(default=datetime.datetime.utcnow)
    UNIDAD = fields.EmbeddedDocumentField(UnidadPrivadaField)
    HABILITADO = fields.BooleanField()

class Usuarios(Document):
    NOMBRE = fields.StringField(required=True)
    CORREO = fields.EmailField()
    PASSWORD = fields.StringField(required=True)
    TELEFONO = fields.StringField(required=True)
    TIPO_DOCUMENTO = fields.StringField(required=True)
    NUMERO_DOCUMENTO = fields.StringField(required=True)
    ASIGNACION_PH = fields.ListField(fields.EmbeddedDocumentField(AsignacionPHField))
    ASIGNACION_UP = fields.ListField(fields.EmbeddedDocumentField(AsignacionUPField))
    HABILITADO = fields.BooleanField()

    meta = {'indexes': [
        {'fields': ['$CORREO']}
    ]}

    @property
    def user__username(self):
        return self.CORREO

    def __unicode__(self):
        return self.CORREO