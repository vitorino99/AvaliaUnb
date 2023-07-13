import MySQLdb
from flask import flash
from flask_login import UserMixin
from database import execute_query


class Avaliacoes(UserMixin):
    def __init__(self,ID, Estudante_ID, Turma_ID, Nota, Comentario, Nome_estudante, matricula):
        self.ID = ID
        self.Estudante_ID = Estudante_ID
        self.Turma_ID = Turma_ID
        self.Nota = Nota
        self.Comentario = Comentario
        self.Nome_estudante = Nome_estudante
        self.matricula = matricula

    
    
class AvaliacoesDAO:
    def __init__(self):
        pass
    

            
    def listar_avalicacoes(id_turma):
 
        query = "SELECT a.ID, a.Estudante_ID, a.Turma_ID, a.Nota, a.Comentario, e.Nome, e.Matricula FROM avaliacoes a JOIN estudantes e ON a.Estudante_ID = e.ID WHERE a.Turma_ID = %s" 
        values = (id_turma,)
        cursor = execute_query(query, values)
        result = cursor.fetchall()
                    
        avaliacoes = []
        if result:
            for x in result:
                avaliacao = Avaliacoes(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                avaliacoes.append(avaliacao)     
            return avaliacoes
        else:
            return None
        
    def avaliar(nota, comentario, turma_id, id_usuario):                    
            query = "INSERT INTO avaliacoes (Nota, Estudante_ID, Comentario, Turma_ID) VALUES (%s, %s, %s, %s)"
            values = (nota, id_usuario, comentario, turma_id)
            execute_query(query, values)
            
    def get_by_id(id):
            
        query = "SELECT * FROM avaliacoes WHERE ID = %s"
        values = (id,)  # Adicione uma vírgula para criar uma tupla
        cursor = execute_query(query, values)
        result = cursor.fetchone()
                    
                
        # Defina as descrições das colunas
        return result
    
    def editar_comentario(comentario_id, nova_nota, novo_comentario):
        query = "UPDATE avaliacoes SET Nota = %s, Comentario = %s WHERE id = %s"
        values = (nova_nota,novo_comentario,comentario_id,)

        execute_query(query, values)

        