import conexao
import numpy as np
import pandas as pd
from datetime import datetime

class Genero:
    
    CAMINHO_DB = '../DB/fat'
    DB_NOME = 'fat_genero'
    EXTENS_DB = '.csv'
    SEP = ';'
    TBL_FAT_GENERO = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def tabelaGeneros(self):
        # inicializa variaveis
        confianca = []
        hora = []
        id_dim_genero = []
        id_dim_data = []
        guids = []
        
        # carrega dimensões
        dim_genero = conexao.Conexao().carregaDimensao('../DB/dim/dim_genero.csv')
        
        # carrega os dados da fato
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'gênero':
                            for item_chave, item_valor in atributo.items():
                                if item_chave == 'confiança':
                                    confianca.append(item_valor)
                                if item_chave == 'valor':
                                    for indice in dim_genero:
                                        if indice[1] == item_valor:
                                            id_dim_genero.append(indice[0])
                                    guids.append(chave)
                        if item == 'data':
                            id_data = datetime.strptime(atributo, '%Y-%m-%d %H:%M:%S.%f').date()
                            hora_data = datetime.strptime(atributo, '%Y-%m-%d %H:%M:%S.%f').time()
                            id_dim_data.append(id_data)
                            hora.append(hora_data)
                             
        ids = [i + 1 for i in range(0, len(guids))]
        
        fato = {'id_fato_genero': ids, 
                'id_genero': id_dim_genero, 
                'vlr_confianca': confianca,
                'data': id_dim_data,
                'hora': hora,
                'guid': guids}
        
        return pd.DataFrame.from_dict(fato)
    
    def fatoGenero(self):
        df = self.tabelaGeneros()
        df.to_csv(self.TBL_FAT_GENERO, index=False ,sep=self.SEP)
