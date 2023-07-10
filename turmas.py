import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func


class Turmas(UserMixin):
    def __init__(self,ID, periodo, professor, horario, local, cod_disciplina, cod_departamento):
        self.id = ID
        self.cod_disciplina = cod_disciplina
        self.professor = professor
        self.cod_departamento = cod_departamento
        self.horario = horario
        self.periodo = periodo
        self.periodo = local
    
    
class TurmasDAO:
    def __init__(self):
        pass
    
   
    def cadastrar(periodo, professor, horario, local, cod_disciplina, nome_departamento):                    
            # Conecte-se ao banco de dados
            db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
            cursor = db.cursor()
                    
            # Execute a consulta SQL para inserir os dados na tabela de estudantes
                    
            query0 = "SELECT cod FROM departamentos WHERE Nome = %s" 
            values = (nome_departamento,)
            
            cursor.execute(query0,values,)
            
            result = cursor.fetchone()
           
                   
            query = "INSERT INTO turmas (periodo, professor, horario, local, cod_disciplina, cod_departamento) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (periodo, professor, horario, local, cod_disciplina, result[0])
            cursor.execute(query, values)
                    
            # Confirme as alterações no banco de dados
            db.commit()
                    
            # Feche a conexão com o banco de dados
            db.close()   
   
    def listar_todas():
            
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT * FROM turmas"
        cursor.execute(query)
        # Obtenha o resultado da consulta
        result = cursor.fetchall()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        estudantes = []
        if result:
            for x in result:
                estudante = Turmas(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                estudantes.append(estudante)     
            return estudantes
        else:
            return None

    def buscar(id_turma):
            
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT * FROM turmas WHERE ID = %s "
        values = (id_turma,)
        cursor.execute(query, values)
        # Obtenha o resultado da consulta
        result = cursor.fetchone()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        if result:
            estudante = Turmas(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
            return estudante
        else:
            return None

            
    def listar_avalicacoes(id_turma):
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT * FROM avaliacoes WHERE Turma_ID = %s" 
        values = (id_turma,)
        cursor.execute(query, values)
        # Obtenha o resultado da consulta
        result = cursor.fetchall()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        estudantes = []
        if result:
            for x in result:
                estudante = Turmas(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                estudantes.append(estudante)     
            return estudantes
        else:
            return None
        
    def melhores_avaliacoes():
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT * FROM MaioresAvaliacoes" 
        cursor.execute(query)
        # Obtenha o resultado da consulta
        result = cursor.fetchall()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        return result
        

    def remover_turma(turma_id):
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()

        query = "DELETE FROM turmas where ID = %s"
        values = (turma_id,)
        cursor.execute(query, values)
        

        db.commit()

        cursor.close()
        db.close()
