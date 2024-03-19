from flask import Flask, render_template
from app import db
from app.controllers.usuario_controller import usuario_blueprint
from app.controllers.renta_controller import renta_blueprint
from app.controllers.pelicula_controller import pelicula_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(renta_blueprint)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/gestion_usuario')
def gestion_usuario():
    return render_template('usuario/gestion_usuario.html')
@app.route('/gestion_renta')
def gestion_renta():
    return render_template('renta/gestion_rentas.html')
@app.route('/gestion_peliculas')
def gestion_pelicula():
    return render_template('pelicula/gestion_peliculas.html')



if __name__ == '__main__':
    app.run(debug=True)  # Habilitar la depuración