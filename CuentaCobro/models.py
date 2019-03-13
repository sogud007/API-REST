from django.db import models

from mongoengine import Document, EmbeddedDocument, fields, LazyReferenceField
from PropHorizontal.models import Propiedades_Horizontales
from Cobro.models import Cobros
from Comprobante.models import Comprobantes
import datetime

class UnidadPrivadaField(EmbeddedDocument):
    IDENTIFICADOR = fields.StringField(required=True)
    GRUPO = fields.StringField(required=True)
    UNIDAD_PRIVADA_ID = fields.LazyReferenceField('Unidades_Privadas', passthrough=False, dbref=False)

class PeriodoCobroField(EmbeddedDocument):
    FECHA_INICIAL = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_FINAL = fields.DateTimeField(default=datetime.datetime.utcnow)

class ElementoField(EmbeddedDocument):
    DESCRIPCION = fields.StringField(required=True)
    VALOR = fields.IntField()
    COBRO_ID = fields.LazyReferenceField(Cobros, passthrough=False, dbref=False)

class DireccionField(EmbeddedDocument):
    PAIS = fields.StringField(required=True)
    DEPARTAMENTO = fields.StringField(required=True)
    MUNICIPIO = fields.StringField(required=True)
    DIRECCION = fields.StringField(required=True)

class PropiedadHorizontalField(EmbeddedDocument):
    PROPIEDAD_ID = fields.LazyReferenceField(Propiedades_Horizontales, passthrough=False, dbref=False)
    NOMBRE = fields.StringField(required=True)
    DIRECCION = fields.EmbeddedDocumentField(DireccionField)
    NIT = fields.StringField(required=True)

class ComprobanteField(EmbeddedDocument):
    PERIODO = fields.StringField(required=True)
    VALOR_PAGO = fields.IntField()
    FECHA_PAGO = fields.DateTimeField(default=datetime.datetime.utcnow)
    COMPROBANTE_ID = fields.LazyReferenceField(Comprobantes, passthrough=False, dbref=False)

class Cuenta_Cobro(Document):
    UNIDAD_PRIVADA = fields.EmbeddedDocumentField(UnidadPrivadaField)
    PERIODO = fields.StringField(required=True)
    CONSECUTIVO = fields.StringField(required=True)    
    FECHA_CUENTA_COBRO = fields.DateTimeField(default=datetime.datetime.utcnow)
    PERIODO_COBRO = fields.EmbeddedDocumentField(PeriodoCobroField)
    ELEMENTOS = fields.ListField(fields.EmbeddedDocumentField(ElementoField))
    INTERESES_CAUSADOS = fields.FloatField()
    SALDO_INTERESES = fields.FloatField()
    SALDO_CAPITAL = fields.FloatField()
    VALOR_TOTAL = fields.FloatField()
    PROPIEDAD_HORIZONTAL = fields.EmbeddedDocumentField(PropiedadHorizontalField)
    COMPROBANTE = fields.EmbeddedDocumentField(ComprobanteField)
    DOCUMENTO = fields.FileField()
    HABILITADO = fields.BooleanField()