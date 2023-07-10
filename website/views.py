import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, login_required, logout_user, current_user
from disciplina import DisicplinaDAO
from turmas import TurmasDAO
from avaliacoes import AvaliacoesDAO
from denuncias import DenunciasDAO
from werkzeug.utils import secure_filename
from estudantes import EstudanteDAO
from departamento import DepartamentoDAO
from professores import ProfessoresDAO
import base64
from PIL import Image
from io import BytesIO
from website.auth import signup

views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@login_required
@views.route('/cadastrar-disciplina', methods=["GET", "POST"])
def cadastrar_disciplina():
    if current_user.is_admin == False:
        flash("Esse recurso está acessivel apenas para administradores", category="error")
        return redirect(url_for('views.home'))
        
    if request.method == 'POST':
        cod_disciplina = request.form.get("cod_disciplina")
        nome_disciplina = request.form.get('nome_disciplina')
        nome_departamento = request.form.get('nome_departamento')
        DisicplinaDAO.cadastrar(cod_disciplina, nome_disciplina,nome_departamento)
        flash("Disciplina cadastrada", category="success")
        
    return render_template('cadastrar_disciplinas.html', user=current_user)

@login_required
@views.route('/cadastrar-turmas', methods=["GET", "POST"])
def cadastrar_turmas():
    if current_user.is_admin == False:
        flash("Esse recurso está acessivel apenas para administradores", category="error")
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        periodo = request.form.get("periodo")
        professor = request.form.get("professor")
        horario = request.form.get("horario")
        local = request.form.get("local")
        cod_disciplina = request.form.get('cod_disciplina')
        departamento = request.form.get('departamento')
        TurmasDAO.cadastrar(periodo, professor,horario, local, cod_disciplina,departamento)
        flash("Disciplina cadastrada", category="success")
        
    return render_template('cadastrar_turmas.html', user=current_user)

@login_required
@views.route('/cadastrar-professores', methods=["GET", "POST"])
def cadastrar_professores():
    if current_user.is_admin == False:
        flash("Esse recurso está acessivel apenas para administradores", category="error")
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        professor = request.form.get("professor")
        email = request.form.get("email")
        nome_departamento = request.form.get("departamento")
        departamento  = DepartamentoDAO.buscar(nome_departamento)
        ProfessoresDAO.cadastrar(professor,email,departamento)
        flash("Professor cadastrado", category="success")
        
    return render_template('cadastrar_professores.html', user=current_user)

@login_required
@views.route('/turmas', methods=["GET"])
def turmas():
    if request.method == 'GET':
        turmas = TurmasDAO.listar_todas()
        melhores_turmas = TurmasDAO.melhores_avaliacoes()
        
    return render_template('turmas.html', turmas=turmas, user=current_user, melhores_turmas=melhores_turmas)

@login_required
@views.route('/turmas/<int:id_turma>', methods=["GET", "POST"])
def detalhar_turma(id_turma):
    if request.method == 'GET':
        turma = TurmasDAO.buscar(id_turma)
    if request.method == 'POST':
        nota = request.form.get('nota')
        comentario = request.form.get('comentario')
        turma = TurmasDAO.buscar(id_turma)
        turma_id = turma.id
        id_usuario = current_user.id
        AvaliacoesDAO.avaliar(nota, comentario, turma_id, id_usuario)
        flash("Avaliação adicionada", category="success")
    avaliacoes = AvaliacoesDAO.listar_avalicacoes(id_turma)
    return render_template('detalhar_turma.html', turma=turma, user=current_user, avaliacoes=avaliacoes)

@login_required
@views.route('/denuncias', methods=["GET"])
def listar_denuncias():
    if current_user.is_admin == False:
        flash("Esse recurso está acessivel apenas para administradores", category="error")
        return redirect(url_for('views.home'))
    if request.method == 'GET':
        denuncias = DenunciasDAO.listar_denuncias()
        return render_template('denuncias.html', user=current_user, denuncias=denuncias)
    
@login_required
@views.route('/denunciar/<int:Estudante_ID>/avaliacao/<int:ID>', methods=["POST"])
def denunciar_avaliacao(Estudante_ID, ID):
    if request.method == 'POST':
        id_avaliacao = ID
        estudante_id = Estudante_ID
        denuncia = DenunciasDAO.buscar_denuncia(id_avaliacao)
        if not denuncia:
            DenunciasDAO.denunciar(id_avaliacao, estudante_id)
        else:
            ID = denuncia[0]
            ocorrencias = denuncia[4]
            ocorrencias += 1
            if denuncia[1] == current_user.id:
                flash("Você já realizou uma denuncia", category="error")
            else:
                DenunciasDAO.atualizar(ocorrencias, ID)
                flash("Denuncia feita", category="success")
        return redirect(request.referrer or url_for('views.home'))

@login_required
@views.route('remover-comentario/<int:comentario_id>', methods=["POST"])
def remover_avaliacao(comentario_id):
    if current_user.is_admin == False:
        flash("Esse recurso está acessivel apenas para administradores", category="error")
    elif request.method == 'POST':
        flash("Denuncia feita", category="success")
        DenunciasDAO.remover_avaliacao(comentario_id)
    return redirect(request.referrer or url_for('views.home'))  


@views.route('deletar-conta/<int:estudante_id>', methods=["POST", "GET"])
def deletar_conta(estudante_id):
    if request.method == 'POST':
        flash("Conta apagada", category="success")
        logout_user()
        EstudanteDAO.remover_estudante(estudante_id)
        return redirect(url_for('views.home')) 
    if request.method == "GET":
        flash("Conta apagada", category="success")
        logout_user()
        return redirect(request.referrer or url_for('views.signup')) 


@login_required
@views.route('detalhar-avaliacao/<int:id_avaliacao>', methods=["GET", "POST"])
def detalhar_avaliacao(id_avaliacao):
    if request.method == 'GET':
        return render_template('detalhar_avaliacao.html', user=current_user, id_avaliacao= id_avaliacao)
    if request.method == 'POST':
        nota = request.form.get("nota")
        comentario = request.form.get('comentario')
        avaliacao = AvaliacoesDAO.get_by_id(id_avaliacao)
        if avaliacao[1] != current_user.id:
            flash("Esse recurso está acessivel apenas para administradores", category="error")
            return redirect(request.referrer or url_for('views.home'))
        else:
            AvaliacoesDAO.editar_comentario(id_avaliacao,nota, comentario)
            flash("Comentario editado", category="success")
            return redirect(request.referrer or url_for('views.home'))
            
# @login_required
# @views.route('editar-avaliacao/', methods=["POST"])
# def editar_avaliacao(avaliacao):
#     if current_user.is_admin == False:
#         flash("Esse recurso está acessivel apenas para administradores", category="error")
#     if avaliacao.Estudante_ID != current_user.id:
#         flash("Você não está autorizado a realizar esse recurso", category="error")
#     elif request.method == 'POST':
#         flash("Denuncia feita", category="success")
#         # DenunciasDAO.remover_avaliacao()
#     return redirect(request.referrer or url_for('views.home'))  

@login_required
@views.route('remover-turma/<int:id_turma>', methods=["POST"])
def remover_turma(id_turma):
    if current_user.is_admin == False:
        flash("Esse recurso está acessivel apenas para administradores", category="error")
    elif request.method == 'POST':
        flash("Turma removida", category="success")
        TurmasDAO.remover_turma(id_turma)
    return redirect(url_for('views.home'))  
    
    
@login_required
@views.route('/perfil', methods=["GET"])
def perfil_usuario():
    if not current_user.id:
        return redirect(url_for('views.home'))
    else:
        userd_id = current_user.id
        user = EstudanteDAO.get_by_id(userd_id)
        if user.foto:
            imagem = base64.b64encode(user.foto).decode('utf-8')
            user.foto = imagem
        return render_template('perfil.html', user=user)



@views.route('/atualizar_perfil', methods=['POST'])
def atualizar_perfil():
    # Obter o ID do estudante e a imagem enviada pelo formulário
    estudante_id = current_user.id 
    imagem = request.files['foto_perfil']
    imagem_final= imagem.read()

    EstudanteDAO.atualizar(estudante_id, imagem_final)

    userd_id = current_user.id
    user = EstudanteDAO.get_by_id(userd_id)
    imagem = base64.b64encode(user.foto).decode('utf-8')
    user.foto = imagem

    # Redirecionar para a página de perfil do usuário se algo der errado
    return render_template('perfil.html', user=user)