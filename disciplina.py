import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func


class Disciplina(UserMixin):
    def __init__(self, ID, nome, departamento_id):
        self.id = ID
        self.nome = nome
        self.departamento_id = departamento_id
    
    
class DisicplinaDAO:
    def __init__(self):
        pass
    
    def cadastrar(cod_disciplina, nome_disciplina, nome_departamento):
                    
        # Conecte-se ao banco de dados
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                    
        query = "SELECT cod FROM departamentos WHERE nome = %s"
        values = (nome_departamento,)
        cursor.execute(query, values)
        
        departamento_id = cursor.fetchone()

        if departamento_id:
            # Insere a nova disciplina na tabela "disciplinas"
            query = "INSERT INTO disciplinas (cod, nome, cod_departamento) VALUES (%s,%s, %s)"
            values = (cod_disciplina,nome_disciplina, departamento_id[0])
            cursor.execute(query, values)
            db.commit()

            db.close()
            return "Disciplina cadastrada com sucesso!"
        else:
            db.close()
            return "Departamento não encontrado."
                    
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
            estudante = Disciplina(result[0], result[1], result[2])
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
            estudante = Disciplina(result[0], result[1], result[2], result[3], result[4])
            return estudante
        else:
            return None
            
