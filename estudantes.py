import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func
import base64


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
            # Conecte-se ao banco de dados
            db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
            cursor = db.cursor()
                    
            # Execute a consulta SQL para inserir os dados na tabela de estudantes
                    
            query = "INSERT INTO estudantes (Nome, Endereco, Email, Senha, Curso, matricula) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (first_name, endereco, email, password1, curso, matricula)
            cursor.execute(query, values)
                    
            # Confirme as alterações no banco de dados
            db.commit()
                    
            # Feche a conexão com o banco de dados
            db.close()
   
    def buscar(email):
            
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT * FROM estudantes WHERE Email = %s"
        values = (email,)  # Adicione uma vírgula para criar uma tupla
        cursor.execute(query, values)

        # Obtenha o resultado da consulta
        result = cursor.fetchone()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        if result:
            estudante = Estudantes(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
            return estudante
        else:
            return None
            


    def get_by_id(id):
            
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT * FROM estudantes WHERE ID = %s"
        values = (id,)  # Adicione uma vírgula para criar uma tupla
        cursor.execute(query, values)

        # Obtenha o resultado da consulta
        result = cursor.fetchone()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        if result:
            estudante = Estudantes(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
            return estudante
        else:
            return None
            
    def atualizar(estudante_id, imagem):
        # Converter a imagem para base64
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
        


        # Executar a consulta SQL para inserir a imagem na tabela
        query = "UPDATE estudantes SET Foto = %s WHERE id = %s"
        values = (imagem, estudante_id)

        cursor.execute(query, values)
        db.commit()

    def remover_estudante(estudante_id):
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()

        query = "DELETE FROM estudantes where ID = %s"
        values = (estudante_id,)
        cursor.execute(query, values)
        

        db.commit()

        cursor.close()
        db.close()

        