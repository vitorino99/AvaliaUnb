import MySQLdb
from flask import flash
from flask_login import UserMixin
from database import execute_query


class Disciplina(UserMixin):
    def __init__(self, ID, nome, departamento_id):
        self.id = ID
        self.nome = nome
        self.departamento_id = departamento_id
    
    
class DisciplinaDAO:
    def __init__(self):
        pass
    
    def cadastrar(cod_disciplina, nome_disciplina, nome_departamento):
                    
        # Conecte-se ao banco de dados
                    
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                    
        query = "SELECT cod FROM departamentos WHERE nome = %s"
        values = (nome_departamento,)
        cursor = execute_query(query, values)
        departamento_id = cursor.fetchone()

        if departamento_id:
            # Insere a nova disciplina na tabela "disciplinas"
            query = "INSERT INTO disciplinas (cod, nome, cod_departamento) VALUES (%s,%s, %s)"
            values = (cod_disciplina,nome_disciplina, departamento_id[0])
            execute_query(query, values)
            return "Disciplina cadastrada com sucesso!"
        else:
            return "Departamento não encontrado."
                    
    def buscar(email):                    
                
                
        query = "SELECT * FROM estudantes WHERE Email = %s"
        values = (email,)  # Adicione uma vírgula para criar uma tupla
        cursor = execute_query(query, values)
        result = cursor.fetchall()
                    
        # Feche a conexão com o banco de dados
                
        # Defina as descrições das colunas
        if result:
            estudante = Disciplina(result[0], result[1], result[2])
            return estudante
        else:
            return None
            

            
