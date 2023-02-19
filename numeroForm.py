from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField
from wtforms.fields import EmailField
class UseForm(Form):
    numero=StringField("Numero")
    numeroDinamicos=StringField("Numero")
 