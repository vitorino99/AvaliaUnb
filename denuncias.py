import MySQLdb
from flask import flash
from flask_login import UserMixin
from sqlalchemy.sql import func


class Denuncias(UserMixin):
    def __init__(self,ID, Estudante_ID, Comentario, Nome, Matricula, Comentario_ID, Ocorrencias):
        self.ID = ID
        self.Estudante_ID = Estudante_ID
        self.Comentario = Comentario
        self.Nome = Nome
        self.Matricula = Matricula
        self.Comentario_ID = Comentario_ID 
        self.Ocorrencias = Ocorrencias
    
class DenunciasDAO:
    def __init__(self):
        pass
    
    def denunciar(avaliacao_id, estudante_id):
            # Conecte-se ao banco de dados
            db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
            cursor = db.cursor()
                    
            # Execute a consulta SQL para inserir os dados na tabela de estudantes
                    
            query = "INSERT INTO denuncias(avaliacao_ID, Estudante_ID, ocorrencias) VALUES (%s, %s,%s)"
            values = (avaliacao_id,estudante_id,1)
            cursor.execute(query, values)
                    
            # Confirme as alterações no banco de dados
            db.commit()
                    
            # Feche a conexão com o banco de dados
            db.close()

            
    def listar_denuncias():
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT DISTINCT d.ID, d.Estudante_ID ,a.Comentario, e.Nome, e.matricula, a.ID as Comentario_ID, d.ocorrencias FROM denuncias d JOIN avaliacoes a ON d.avaliacao_ID = a.ID JOIN estudantes e ON a.Estudante_ID = e.ID;"
        cursor.execute(query)
        # Obtenha o resultado da consulta
        result = cursor.fetchall()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        denuncias = []
        if result:
            for x in result:
                denuncia = Denuncias(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                denuncias.append(denuncia)     
            return denuncias
        else:
            return None
        
        
        
    def remover_avaliacao(comentario_id):
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()

        query = "CALL apagar_comentario_denunciado(%s);"
        values = (comentario_id,)
        cursor.execute(query, values)
        

        db.commit()

        cursor.close()
        db.close()

    def buscar_denuncia(id):
            
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT DISTINCT d.ID, d.Estudante_ID, d.Professor_ID, d.avaliacao_ID, d.ocorrencias FROM denuncias d JOIN avaliacoes a ON d.avaliacao_ID = a.ID WHERE a.ID = %s"
        values = (id,)  # Adicione uma vírgula para criar uma tupla
        cursor.execute(query, values)

        # Obtenha o resultado da consulta
        result = cursor.fetchone()
                    
        # Feche a conexão com o banco de dados
        db.close()
                
        # Defina as descrições das colunas
        if result:
            return result
        
        return None

    def atualizar(ocorrencias, id):
        # Converter a imagem para base64
        db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        cursor = db.cursor()
        


        # Executar a consulta SQL para inserir a imagem na tabela
        query = "UPDATE denuncias SET ocorrencias = %s WHERE ID = %s"
        values = (ocorrencias, id)

        cursor.execute(query, values)
        db.commit()
        