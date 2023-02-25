
#Referenciamos Flask
from flask import Flask, render_template
from flask import request
import forms 
import numeroForm 

app= Flask(__name__) 

#Rutas de paginas decorador
@app.route("/formulario")
def formulario():
    return render_template("formulario.html") 

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    alum_form= forms.UseForm(request.form)

    if request.method=='POST':
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)


    return render_template("Alumnos.html",form=alum_form) 

@app.route("/cajasDinamicas",methods=['GET','POST'])
def cajasDinamicas():
    alum_form= numeroForm.UseForm(request.form)
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
        
        for element in request.form:
            
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