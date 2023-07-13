from flask import flash
from database import execute_query


class Departamento():
    def __init__(self,cod, nome):
        self.cod = cod
        self.nome = nome

    
    
class DepartamentoDAO:
    def __init__(self):
        pass
    
   
    def buscar(nome_departamento):
        # Execute a consulta SQL para inserir os dados na tabela de estudantes
                
                
        query = "SELECT cod FROM departamentos WHERE Nome = %s "
        values = (nome_departamento,)
        cursor = execute_query(query, values)
        result = cursor.fetchone() 
                    
        # Feche a conexão com o banco de dados
                
        # Defina as descrições das colunas
        return result[0]

    