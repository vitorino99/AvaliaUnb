import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func


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
            # Conecte-se ao banco de dados
            db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
            cursor = db.cursor()
                    
            # Execute a consulta SQL para inserir os dados na tabela de estudantes
                    
            query = "INSERT INTO professores (Nome, Email, Departamento_ID) VALUES (%s, %s, %s)" 
            values = (professor, email, codigo_departamento,)
            
            cursor.execute(query,values)
            
           
                    
            # Confirme as alterações no banco de dados
            db.commit()
                    
            # Feche a conexão com o banco de dados
            db.close()   
   