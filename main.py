from persistence import MySQL
from multiprocessing import Pool

global mysql

mysql = MySQL()

def stage(tabela):
    parametro = 'Carga Stage ' + tabela.lower().capitalize()
    tabela_stage = 'stg_' + tabela.lower()
    
    switch = {
        'cartaz': "INSERT INTO STG_CARTAZ (ID_cartaz, HashID, Data_documento, Id_genero, Id_dispositivo) VALUES (%s, %s, %s, %s, %s)",
        'documento': "INSERT INTO STG_DOCUMENTO (HashID, Data_documento, Id_dispositivo, Nome, Largura, Altura, Local, Imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        'pessoa' : "INSERT INTO STG_PESSOA (HashID, Data_documento, Id_genero, Confianca_G, Idade, Confianca_I, Id_dispositivo, Imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        'sentimento' : "INSERT INTO STG_SENTIMENTO (Id_emocao, Valor, Confianca, HashID, Data_documento, Id_genero, Id_dispositivo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    }
    
    try:
        query_select = mysql.consultaParametro(parametro)
        resultset = mysql.consultaTransacional(query_select)
        mysql.truncate_etl(tabela_stage)
        query_insercao = switch.get(tabela.lower(), '')
        mysql.inserir_etl(resultset, query_insercao)
        info = '[INFO] Carga da ' + tabela_stage + ' concluída'
        print(info)
    except:
        erro = '[ERRO] Falha na carga da ' + tabela_stage
        print(erro)
        
def fato(tabela):
    parametro = 'Carga Fato ' + tabela.lower().capitalize()
    tabela_fato = 'fat_' + tabela.lower()
    
    switch = {
        'cartaz' : "INSERT INTO fat_cartaz (ID, ID_cartaz, HashID, Data_documento, Data, Hora_documento, Minuto_documento, Id_genero, Id_dispositivo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        'documento' : "INSERT INTO fat_documento (ID, HashID, Data_documento, Data, Hora_documento, Minuto_documento, Id_dispositivo, Nome, Largura, Altura, Local, Imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        'pessoa' : "INSERT INTO fat_pessoa (ID, HashID, Data_documento, Data, Hora_documento, Minuto_documento, Id_genero, Confianca_G, Idade, Confianca_I, Id_dispositivo, Imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        'sentimento' : "INSERT INTO fat_sentimento (ID, Id_emocao, Valor, Confianca, HashID, Data_documento, Data, Hora_documento, Minuto_documento, Id_genero, Id_dispositivo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    }
    
    try:
        query_select = mysql.consultaParametro(parametro)
        resultset = mysql.consultaDW(query_select)
        query_insercao = switch.get(tabela.lower(), '')
        mysql.inserir_etl(resultset, query_insercao)
        info = '[INFO] Carga da ' + tabela_fato + ' concluída'
        print(info)
    except:
        erro = '[ERRO] Falha na carga da ' + tabela_fato
        print(erro)
        
if __name__ == "__main__":
    
    tabelas = ['cartaz', 'documento', 'pessoa', 'sentimento']
    
    try:
        while True:
            pool = Pool(processes=4)
            pool.map(stage, tabelas, chunksize=2)
            pool.map(fato, tabelas, chunksize=2)
            pool.close()
            pool.join()
    except:
        print('[ERRO] Ocorreu um erro na paralelização')
        pass
