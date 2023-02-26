from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField
from wtforms.fields import EmailField
from wtforms import IntegerField
from wtforms import validators
class UseFormulario(Form):
    #alumnos
    matricula=StringField("Matricula")
    nombre=StringField("Nombre")
    apaterno=StringField("Apaterno")
    email=EmailField("Correo")

    #Cajas Dinamicas
    numero=StringField("Numero")
    numeroDinamicos=StringField("Numero")

class LoginForm(Form):
    username=StringField('usuario',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=15,message='No cumple con la longitud para el campo')])
    password=StringField('password',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=15,message='No cumple con la longitud para el campo')])
    
def mi_Validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',[
                            validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=4, max=10, message='long de campo 4 min and 5 max')])
    nombre = StringField('Nombre',[
                         validators.DataRequired(message='El campo es requerido')])
    apaterno = StringField('Apaterno', [mi_Validacion])
    amaterno = StringField('Amaterno')
    email = EmailField('Email')


class DynamicForm(FlaskForm):
    pass