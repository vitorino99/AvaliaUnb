import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func
import base64
from database import execute_query


class Estudantes(UserMixin):
    def __init__(self, ID, nome, endereco, email, senha, matricula, curso, foto, is_admin):
        self.id = ID
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.senha = senha
        self.matricula = matricula
        self.curso= curso
        self.foto = foto
        self.is_admin = is_admin
    
    
class EstudanteDAO:
    def __init__(self):
        pass
    
    def cadastrar(email, first_name, password1, password2, endereco, matricula, curso):                                        
            query = "INSERT INTO estudantes (Nome, Endereco, Email, Senha, Curso, matricula, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (first_name, endereco, email, password1, curso, matricula, 0)

            execute_query(query, values)
   
    def buscar(email):
        query = "SELECT * FROM estudantes WHERE Email = %s"
        values = (email,)

        cursor = execute_query(query, values)
        result = cursor.fetchone()  # Use fetchone() para obter apenas um resultado

        if result:
            estudante = Estudantes(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
            return estudante
        else:
            return None

            


    def get_by_id(id):
        query = "SELECT * FROM estudantes WHERE ID = %s"
        values = (id,)  # Adicione uma vírgula para criar uma tupla
        cursor = execute_query(query, values)
        result = cursor.fetchone() 

                
                
        # Defina as descrições das colunas
        if result:
            estudante = Estudantes(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
            return estudante
        else:
            return None
            
    def atualizar(estudante_id, imagem):
        # Converter a imagem para base64

        

        # Executar a consulta SQL para inserir a imagem na tabela
        query = "UPDATE estudantes SET Foto = %s WHERE id = %s"
        values = (imagem, estudante_id)

        execute_query(query, values) 

    def remover_estudante(estudante_id):
        values = (estudante_id,)
        
        query1 = "DELETE FROM denuncias WHERE Estudante_ID = %s"
        execute_query(query1, values)        
        
        query0 = "DELETE FROM avaliacoes WHERE Estudante_ID = %s"
        execute_query(query0, values)
    
        
        query = "DELETE FROM estudantes where ID = %s"
        execute_query(query, values)


        