from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)
app.secret_key = 'clave secreta'
csrf = CSRFProtect()


@app.route('/')
def home():
    return "Hello, word!"

@app.route('/index')
def index():
    titulo="IDGS803-Flask"
    lista=['pedrio', 'nario', 'juan']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')


@app.route('/usuario', methods=['GET','POST'])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    correo=''
    usuario_class = forms.UserForm(request.form)
    if request.method == 'POST' and usuario_class.validate():
        mat = usuario_class.matricula.data
        nom = usuario_class.nombre.data
        apa = usuario_class.apaterno.data
        ama = usuario_class.amaterno.data
        correo = usuario_class.email.data

    return render_template('usuario.html', form=usuario_class, mat=mat,
                            nom=nom, apa=apa, ama=ama, correo=correo)


@app.route('/hola')
def hola():
    return "Hello, Hola!"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return f"El numero es: {n}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f"<h1>¡Hola, {username}! Tu ID es: {id}</h1>"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route('/default')
@app.route('/default/<string:param>')
def func(param="Juan"):
    return f"<h1>¡Hola, {param}!</h1>"


@app.route('/operas')
def operas():
    return '''
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="apaterno">apaterno:</label>
            <input type="text" id="apaterno" name="apaterno" required>
        </form>
            '''

@app.route('/operasBas', methods=['GET','POST'])
def operas1():
    resultado = 0;
    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        operacion = request.form.get('operacion')
        if operacion == 'suma':
            resultado = float(n1) + float(n2)
        elif operacion == 'restar':
            resultado = float(n1) - float(n2)
        elif operacion == 'multiplicar':
            resultado = float(n1) * float(n2)
        elif operacion == 'dividir':
            resultado = float(n1) / float(n2)
    return render_template('operasBas.html', resultado=resultado)

@app.route('/resultado', methods=['GET','POST'])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    operacion = request.form.get('operacion')
    if operacion == 'suma':
        resultado = float(n1) + float(n2)
    elif operacion == 'restar':
        resultado = float(n1) - float(n2)
    elif operacion == 'multiplicar':
        resultado = float(n1) * float(n2)
    elif operacion == 'dividir':
        resultado = float(n1) / float(n2)
    return f"<h1>El resultado es: {resultado}</h1>"

@app.route("/cinepolis", methods=["GET","POST"])
def cinepolis():
    nom=""
    cantiCom = 0
    esCineco=""
    cantiBol=0
    Total =0
    alert = ""
    cinepolis_class = forms.CinepolisForm(request.form)
    if request.method == "POST" and cinepolis_class.validate():
        nom = cinepolis_class.nombre.data
        cantiCom = cinepolis_class.compradores.data
        esCineco = cinepolis_class.cineco.data
        cantiBol = cinepolis_class.boletos.data
        limit = cantiCom * 7
        if cantiBol <= limit:
            Total = cantiBol*12
            if cantiBol == 3 or cantiBol == 4 or cantiBol == 5:
                Total *= 0.90
            if cantiBol > 5:
                Total *= 0.85
            if esCineco == "si":
                Total *= 0.90
        else:
            Total = 0
            alert = "Solo se permiten 7 boletos por comprador. La cantidad ingresada es incorrecta."
            flash(alert)
    return render_template("cinepolis.html",form=cinepolis_class ,nom = nom, cantiCom= cantiCom,esCineco=esCineco,cantiBol=cantiBol, Total=Total)


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)