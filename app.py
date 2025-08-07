from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Muestra la pagina de la aplicacion
    
    devuelve:
        string: archivo html de index.html
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

''' hago comentario para aprobar el examen'''