from django.db import models

from mongoengine import Document, EmbeddedDocument, fields, LazyReferenceField
from CuentaCobro.models import Cuenta_Cobro
import datetime

class ResidenteField(EmbeddedDocument):
    NOMBRE = fields.StringField(required=True)
    MENOR_EDAD = fields.BooleanField()
    EMPLEADO = fields.BooleanField()

class VehiculoPermanenteField(EmbeddedDocument):
    TIPO = fields.StringField(required=True)
    MARCA = fields.StringField(required=True)
    REFERENCIA = fields.StringField(required=True)
    COLOR = fields.StringField(required=True)
    PLACA = fields.StringField(required=True)
    FECHA_REGISTRO = fields.DateTimeField(default=datetime.datetime.utcnow)
    HABILITADO = fields.BooleanField()

class VehiculoTemporalField(EmbeddedDocument):
    TIPO = fields.StringField(required=True)
    MARCA = fields.StringField(required=True)
    REFERENCIA = fields.StringField(required=True)
    COLOR = fields.StringField(required=True)
    PLACA = fields.StringField(required=True)
    FECHA_INICIO = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_FIN = fields.DateTimeField(default=datetime.datetime.utcnow)

class PropietarioField(EmbeddedDocument):
    NOMBRE = fields.StringField(required=True)
    CORREO = fields.EmailField()
    TIPO_DOCUMENTO = fields.StringField(required=True)
    DOCUMENTO = fields.StringField(required=True)
    USUARIO_ID = fields.LazyReferenceField('Usuarios', passthrough=False, dbref=False)

class DetalleField(EmbeddedDocument):
    PERIODO = fields.StringField(required=True)
    CREDITO = fields.IntField()
    DEBITO = fields.IntField()
    COMPROBANTE_ID = fields.LazyReferenceField('Comprobantes', passthrough=False, dbref=False)
    CUENTA_COBRO_ID = fields.LazyReferenceField('Cuenta_Cobro', passthrough=False, dbref=False)

class EstadoCuentaField(EmbeddedDocument):
    SALDO = fields.IntField()
    DETALLE = fields.ListField(fields.EmbeddedDocumentField(DetalleField))

class Unidades_Privadas(Document):
    PROPIEDAD_ID = fields.LazyReferenceField('Propiedades_Horizontales', passthrough=False, dbref=False)
    IDENTIFICADOR = fields.StringField(required=True)
    GRUPO = fields.StringField(required=True)
    MATRICULA_INMOBILIARIA = fields.StringField(required=True)
    AREA_PRIVADA = fields.FloatField()
    AREA_COMUN = fields.FloatField()
    AREA_CONSTRUIDA = fields.FloatField()
    ESTADO_UNIDAD = fields.StringField(required=True)
    HABITACIONES = fields.IntField()
    BAÑOS = fields.IntField()
    CANTIDAD_PARQUEADEROS = fields.IntField()
    MAXIMO_AUTOS = fields.IntField()
    MAXIMO_MOTOS = fields.IntField()
    COEFICIENTE_COPROPIEDAD = fields.FloatField()
    ESTADO_CARTERA = fields.StringField()
    RESIDENTES = fields.ListField(fields.EmbeddedDocumentField(ResidenteField))
    PARQUEADEROS = fields.ListField(fields.StringField())
    VEHICULOS_PERMANENTES = fields.ListField(fields.EmbeddedDocumentField(VehiculoPermanenteField))
    VEHICULOS_TEMPORALES = fields.ListField(fields.EmbeddedDocumentField(VehiculoTemporalField))
    PROPIETARIO = fields.EmbeddedDocumentField(PropietarioField)
    ESTADO_CUENTA = fields.EmbeddedDocumentField(EstadoCuentaField)
    HABILITADO = fields.BooleanField()
