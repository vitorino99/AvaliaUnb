from flask import Flask
import mysql.connector
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from estudantes import EstudanteDAO



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "meusegredosecreto"
    from .views import views
    from .auth import auth    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        estudante = EstudanteDAO.get_by_id(int(id))
        
        return estudante
        
    
    return app