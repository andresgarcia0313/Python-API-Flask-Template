from flask import Flask
#importamos la clase. Una instancia de esta clase será nuestra aplicación WSGI.
from flask import request
#importamos request para detectar GET POST PUT ...

#A continuación, creamos una instancia de esta clase. El primer argumento es 
# el Nombre del módulo o paquete de la aplicación. es un Atajo conveniente
# para esto que es apropiado para la mayoría de los casos. Esto es necesario
# para que Flask sepa dónde buscar recursos como como plantillas y archivos
# estáticos.__name__

app = Flask(__name__)
# Luego usamos el decorador para decirle a Flask qué URL debe activar nuestra función
@app.route("/")
def index():
    """_summary_
    La función devuelve el mensaje que queremos mostrar en el Explorador. 
    El tipo de contenido predeterminado es HTML, por lo que HTML en la cadena
    será renderizado por el navegador.
    
    Returns:
        _type_: _description_
    """
    return "<p>Bienvenido a la API!</p>"

@app.route('/greet')
def greet():
    return 'Hola, Bienvenido'

@app.route('/user')
def users():
    return 'Mira los usuarios así: <br> use /user/nombredeusuario'

@app.route('/user/<username>', methods=['GET'] )
def show_user_profile(username):
    if request.method == 'GET':
        return {
            "username": username
        }
@app.route('/flask-health-check')
def flask_health_check():
	return "success"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 5000), debug=True)
"""flask run --host=0.0.0.0 --port=5000 --reload """
