from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route('/usuario')
def usuario():
    return render_template('usuario.html')


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

if __name__ == '__main__':
    app.run(debug=True)