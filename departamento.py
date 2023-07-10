import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func


class Departamento():
    def __init__(self,cod, nome):
        self.cod = cod
        self.nome = nome

    
    
class DepartamentoDAO:
    def __init__(self):
        pass
    
   
    def buscar(nome_departamento):
            
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT cod FROM departamentos WHERE Nome = %s "
        values = (nome_departamento,)
        cursor.execute(query, values)
        # Obtenha o resultado da consulta
        result = cursor.fetchone()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        return result[0]

    