from flask import Blueprint, render_template, request, flash, Flask, redirect, url_for
import MySQLdb
from estudantes import Estudantes
import random
from estudantes import EstudanteDAO
auth = Blueprint("auth", __name__)
app = Flask(__name__)
from flask_login import login_user, login_required, logout_user, current_user

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = EstudanteDAO.buscar(email)
        if usuario:
            if usuario.senha == password:
                flash('Logado com sucesso!', category="success")
                login_user(usuario, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Senha incorreta", category="error")
    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        matricula = request.form.get('matricula')
        curso = request.form.get('curso')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        endereco = request.form.get('endereco')
        
        user = EstudanteDAO.buscar(email)
        
        if user:
            flash("Esse usuario já existe", category="error")
        elif len(email) < 7:
            flash("Email invalido", category="error")
        elif password1 != password2:
            flash("As senhas não batem", category="error")
        elif len(first_name) < 2:
            flash("Nome invalido", category="error")
        elif len(password1) < 7:
            flash("Senha fraca", category="error")
        elif len(password1) !=  9:
            flash("Matricula Invalida", category="error")
        else:
            flash("Conta criada", category="success")
            
            EstudanteDAO.cadastrar(email, first_name, password1, password2, endereco, matricula, curso)
            usuario = EstudanteDAO.buscar(email)
            login_user(usuario, remember=True)
            return redirect(url_for('views.home'))
    return render_template('signup.html', user= current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run()