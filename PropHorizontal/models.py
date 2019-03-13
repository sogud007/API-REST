from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, LazyReferenceField
from Usuario.models import Usuarios
from Modulo.models import Modulos
import datetime

# Create your models here.

class DireccionField(EmbeddedDocument):
    PAIS = fields.StringField(required=True)
    DEPARTAMENTO = fields.StringField(required=True)
    MUNICIPIO = fields.StringField(required=True)
    DIRECCION = fields.StringField(required=True)
    TELEFONO = fields.StringField(required=False)

class RepresentanteField(EmbeddedDocument):
    NOMBRE = fields.StringField(required=True)
    TIPO_DOCUMENTO = fields.StringField(required=True)
    NUMERO_DOCUMENTO = fields.StringField(required=True)
    CORREO = fields.LazyReferenceField(Usuarios, passthrough=False, dbref=False)

class UbicacionField(EmbeddedDocument):
    LATITUD = fields.FloatField()
    LONGITUD = fields.FloatField()

class UbicacionField(EmbeddedDocument):
    LATITUD = fields.FloatField()
    LONGITUD = fields.FloatField()

class AdministradorField(EmbeddedDocument):
    NOMBRE = fields.StringField(required=True)
    TELEFONO = fields.StringField(required=True)
    CORREO = fields.EmailField()
    USUARIO_ID = fields.LazyReferenceField(Usuarios, passthrough=False, dbref=False)

class ParqueaderoVisitanteField(EmbeddedDocument):
    TIPO = fields.StringField(required=True)
    CANTIDAD = fields.IntField()

class ParqueaderoField(EmbeddedDocument):
    TIPO = fields.StringField(required=True)
    CANTIDAD = fields.IntField()
    MAXIMO_CARROS = fields.IntField()
    MAXIMO_MOTOS = fields.IntField()
    PARQUEADERO_VISITANTES = fields.EmbeddedDocumentField(ParqueaderoVisitanteField)

class UnidadPrivadaField(EmbeddedDocument):
    IDENTIFICADOR = fields.StringField(required=True)
    GRUPO = fields.StringField(required=True)
    UNIDAD_PRIVADA_ID = fields.LazyReferenceField('Unidades_Privadas', passthrough=False, dbref=False)

class DetalleField(EmbeddedDocument):
    NOMBRE = fields.StringField(required=True)
    PISOS = fields.IntField()
    CANTIDAD = fields.IntField()
    UNIDADES_PRIVADAS = fields.ListField(fields.EmbeddedDocumentField(UnidadPrivadaField))

class GrupoField(EmbeddedDocument):
    IDENTIFICADOR = fields.StringField(required=True)
    CANTIDAD = fields.IntField()
    DETALLE = fields.ListField(fields.EmbeddedDocumentField(DetalleField))

class ModuloField(EmbeddedDocument):
    NOMBRE = fields.StringField(required=True)
    FECHA_INICIO = fields.DateTimeField(default=datetime.datetime.utcnow)
    FECHA_FIN = fields.DateTimeField(default=datetime.datetime.utcnow)
    MODULO_ID = fields.EmailField(Modulos)

class Propiedades_Horizontales(Document):
    NIT = fields.StringField(required=True)
    RAZON_SOCIAL = fields.StringField(required=True)
    DESCRIPCION = fields.StringField()
    DIRECCION = fields.EmbeddedDocumentField(DireccionField)
    REPRESENTANTE = fields.EmbeddedDocumentField(RepresentanteField)
    UBICACION = fields.EmbeddedDocumentField(UbicacionField)
    TIPO = fields.StringField(required=True)
    VALOR_PROMEDIO_ADMINISTRACION = fields.IntField()
    ADMINISTRADOR = fields.EmbeddedDocumentField(AdministradorField)
    CLASE_PROPIEDAD = fields.StringField()
    RESOLUCION = fields.FileField()
    ACTA_CONSEJO = fields.FileField()
    PARQUEADEROS = fields.EmbeddedDocumentField(ParqueaderoField)
    GRUPOS = fields.EmbeddedDocumentField(GrupoField)
    MODULOS = fields.ListField(fields.EmbeddedDocumentField(ModuloField))
    HABILITADO = fields.BooleanField()