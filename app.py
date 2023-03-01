import math
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

valores = {
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "10": 9
    }
english_names = {
        "1": "black",
        "2": "brown",
        "3": "red",
        "4": "orange",
        "5": "yellow",
        "6": "green",
        "7": "blue",
        "8": "violet",
        "9": "gray",
        "10": "white",
        "oro": "gold",
        "plata": "silver"
    }
esp_names = {
            "1": "negro",
            "2": "cafe",
            "3": "rojo",
            "4": "naranja",
            "5": "amarillo",
            "6": "verde",
            "7": "azul",
            "8": "violeta",
            "9": "gris",
            "10": "blanco",
            "oro": "oro",
            "plata": "plata"
        }
@app.route("/resistencia",methods=['GET','POST'])
def calcularResistencia():
    banda1=request.form.get("banda1")
    banda2=request.form.get("banda2")
    banda3=request.form.get("banda3")
    tolerancia= request.form.get("tolerancia")
    if request.method == 'POST':
        banda1_en = english_names[banda1]
        banda2_en = english_names[banda2]
        banda3_en = english_names[banda3]
        tolerancia_en = english_names[tolerancia]

        valor1 = valores[banda1]
        valor2 = valores[banda2]
        multiplicador = math.pow(10, valores[banda3])
        tolerancia_valor = 0.05 if tolerancia == "oro" else 0.1

        valor = (valor1 * 10 + valor2) * multiplicador
        valor_minimo = valor * (1 - tolerancia_valor)
        valor_maximo = valor * (1 + tolerancia_valor)
        #banda1=esp_names[banda1],banda2=esp_names[banda2],banda3=esp_names[banda3],tolerancia=esp_names[tolerancia], banda1_en=banda1_en,banda2_en=banda2_en,banda3_en=banda3_en,tolerancia_en=tolerancia_en, valor=valor,valor_minimo=valor_minimo,valor_maximo=valor_maximo

        return render_template('resistencia.html',banda1=esp_names[banda1],banda2=esp_names[banda2],banda3=esp_names[banda3],tolerancia=esp_names[tolerancia], banda1_en=banda1_en,banda2_en=banda2_en,banda3_en=banda3_en,tolerancia_en=tolerancia_en, valor=valor,valor_minimo=valor_minimo,valor_maximo=valor_maximo)
    return render_template('resistencia.html')




@app.route("/traductor",methods=['GET','POST'])
def traducir():
    result=""
    
    if request.form.get("palabraEng") or request.form.get("palabraEsp"):
        palabraIngles=request.form.get("palabraEng")
        palabraEspanol=request.form.get("palabraEsp")
        f = open('palabras.txt','a')
        f.write(palabraIngles.lower()+' '+palabraEspanol.lower()+'\n')
        f.close()
    elif request.form.get("palabra"):
        palabra=request.form.get("palabra").lower()

        fichero = open('palabras.txt')
        lineas = fichero.readlines()

        for linea in lineas:
            arraySplit=linea.split()
            if arraySplit[0] == palabra:
                result=arraySplit[1]
            elif arraySplit[1] == palabra:
                result=arraySplit[0]

    return render_template('traductor.html',result=result)


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