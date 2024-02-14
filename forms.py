from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class UsersForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa nombre valido')
    ])
    apaterno=StringField('apaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa apellido paterno valido')
    ])
    amaterno=StringField('amaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa apellido materno valido')
    ])
    edad=IntegerField('edad', [
        validators.number_range(min=1, max=20, message='Valor no valido')
    ])
    correo=EmailField('correo', [
        validators.Email(message='Ingrese un correo valido')
    ])