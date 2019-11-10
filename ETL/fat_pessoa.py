import conexao
import numpy as np
import pandas as pd
from datetime import datetime

class Pessoa:
    
    CAMINHO_DB = '../DB/fat'
    DB_NOME = 'fat_pessoa'
    EXTENS_DB = '.csv'
    SEP = ';'
    TBL_FAT_PESSOA= CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def tabelaPessoas(self):
        # inicializa variaveis
        confianca = []
        confianca_idade = []
        vlr_idade = []
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
                        if item == 'idade':
                            for item_chave, item_valor in atributo.items():
                                if item_chave == 'confiança':
                                    confianca_idade.append(item_valor)
                                if item_chave == 'valor':
                                    vlr_idade.append(item_valor)
                            
                             
        ids = [i + 1 for i in range(0, len(guids))]
        
        fato = {'id_fato_pessoa': ids, 
                'id_genero': id_dim_genero, 
                'vlr_confianca_genero': confianca,
                'idade_estimada': vlr_idade,
                'vlr_confianca_idade': confianca_idade,
                'data': id_dim_data,
                'hora': hora,
                'guid': guids}
        
        return pd.DataFrame.from_dict(fato)
    
    def fatoPessoa(self):
        df = self.tabelaPessoas()
        df.to_csv(self.TBL_FAT_PESSOA, index=False ,sep=self.SEP)
