import mysql.connector as conn
from mysql.connector import Error

class MySQL:
    
    def conexaoDW(self):
        conect = None
        
        try:
             conect = conn.connect(host='localhost', 
                                   database='plum_dw',
                                   user='alunos', 
                                   password='alunos')
        
        except Error as e:
            print(e)
        
        return conect
    
    def conexao(self):
        conect = None
        
        try:
             conect = conn.connect(host='localhost', 
                                   database='plum',
                                   user='alunos', 
                                   password='alunos')
        
        except Error as e:
            print(e)
        
        return conect
    
    def consultaTransacional(self, comando):
        conn = self.conexao()
        cursor = conn.cursor()
        
        cursor.execute(comando)
        
        linhas = cursor.fetchall()

        cursor.close()
        conn.close()
        
        return linhas
    
    def consultaDW(self, comando):
        conn = self.conexaoDW()
        cursor = conn.cursor()
        
        cursor.execute(comando)
        
        linhas = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return linhas
    
    def inserir_etl(self, resultset, comando):
        conn = self.conexaoDW()
        
        cursor = conn.cursor()
        
        cursor.executemany(comando, (resultset))
        
        conn.commit()
        
        cursor.close()
        conn.close()

    def truncate_etl(self, tabela):
        conn = self.conexaoDW()
        
        cursor = conn.cursor()
        
        comando = "TRUNCATE TABLE " + tabela
        
        cursor.execute(comando)
        
        cursor.close()
        conn.close()
        
    def consultaParametro(self, nome):
        conn = self.conexaoDW()
        
        cursor = conn.cursor()
        comando = "SELECT Consulta FROM ParametroConsulta WHERE Nome = '" + nome + "'"
        
        cursor.execute(comando)
        
        consulta = cursor.fetchone()

        cursor.close()
        conn.close()
                
        return consulta[0]
        