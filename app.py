from flask import Flask,render_template,redirect,url_for,request, make_response, flash
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
csrf = CSRFProtect(app)

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

@app.route("/cookies", methods = ['GET','POST'])
def cookies():
    reg_user = forms.LoginForm(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@' + passw
        success_message = 'Bienvenido {}'.format(user)
        flash(success_message)
    
    response = make_response(render_template('cookies.html', form = reg_user))
    if len(datos) > 0 :
        response.set_cookie('datos_user', datos)
    
    return response

@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres = valor_cookie.split('@')
    return render_template('saludo.html', nom = nombres[0])


#Rutas de paginas decorador
@app.route("/formulario")
def formulario():
    return render_template("formulario.html") 

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():    
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate() :
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)             
    return render_template('alumnos.html',form=alum_form)

@app.route("/cajasDinamicas",methods=['GET','POST'])
def cajasDinamicas():
    numero=0
    alum_form= forms.UseFormulario(request.form)
    if request.method=='POST':
        numero= request.form.get("numero")
    return render_template("cajasDinamicas.html",form=alum_form,cajas=int(numero)) 

@app.route("/calculador",methods=['GET','POST'])
def calculador():
    if request.method=='POST':
        suma=0
        menor=int(request.form.get('txtNumero0'))
        numerosRepetidos={}
        mayor = int(request.form.get('txtNumero0'))
        print(request.form)

        
        for element in request.form:
          if element!="csrf_token":
            
            if request.form.get(element) not in numerosRepetidos:
                numerosRepetidos[request.form.get(element)] = 0
            numerosRepetidos[request.form.get(element)] =numerosRepetidos[request.form.get(element)]+1 
        
            if int(request.form.get(element))>mayor:
                mayor= int(request.form.get(element))
            
            if int(request.form.get(element))<menor:
                menor= int(request.form.get(element))

            suma+= int(request.form.get(element))
        promedio= suma/len(request.form)
     
    return render_template("resultadoOperaciones.html",suma=suma,mayor=mayor,menor=menor,promedio=promedio,numerosRepetidos=numerosRepetidos) 
        

if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente