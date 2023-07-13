import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func
from database import execute_query


class Professores():
    def __init__(self,id, nome, email, departamento_id):
        self.id = id
        self.nome = nome
        self.email = email
        self.departamento_id = departamento_id
    
    
class ProfessoresDAO:
    def __init__(self):
        pass
    
   
    def cadastrar(professor, email, codigo_departamento):                    
                    
            query = "INSERT INTO professores (Nome, Email, Departamento_ID) VALUES (%s, %s, %s)" 
            values = (professor, email, codigo_departamento,)
            
            cursor = execute_query(query, values)
            result = cursor.fetchone() 
   