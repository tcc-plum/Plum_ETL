import conexao
import numpy as np
import pandas as pd
from datetime import datetime

class Sentimento:
    
    CAMINHO_DB = '../DB/fat'
    DB_NOME = 'fat_sentimento'
    EXTENS_DB = '.csv'
    SEP = ';'
    TBL_FAT_SENTIMENTO = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def pesquisaID(self, emocao, dimensao):
        for indice in dimensao:
            if indice[1] == emocao:
                return indice[0]
            
    def dataHora(self, guid):
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'data':
                            if chave == guid:
                                id_data = datetime.strptime(atributo, '%Y-%m-%d %H:%M:%S.%f').date()
                                hora_data = datetime.strptime(atributo, '%Y-%m-%d %H:%M:%S.%f').time()
                                return id_data, hora_data
        
    
    def tabelaSentimentos(self):
        # inicializa variaveis
        confianca = []
        vlr_resultado = []
        hora = []
        id_dim_emocao = []
        id_dim_data = []
        guids = []
        
        # carrega dimensões
        dim_emocao = conexao.Conexao().carregaDimensao('../DB/dim/dim_emocao.csv')
        
        # carrega os dados da fato
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'sentimentos':
                            for item_chave, item_valor in atributo.items():
                                id_atributo = self.pesquisaID(item_chave, dim_emocao)
                                id_dim_emocao.append(id_atributo)
                                for k1, v1 in item_valor.items():
                                    if k1 == 'confiança':
                                        confianca.append(v1)
                                    if k1 == 'valor':
                                        vlr_resultado.append(v1)
                                guids.append(chave)
        
        for guid in guids:
            data, hora_valor_valor = self.dataHora(guid)
            id_dim_data.append(data)
            hora.append(hora_valor_valor)
                             
        ids = [i + 1 for i in range(0, len(guids))]
        
        fato = {'id_fato_emocao': ids, 
                'id_emocao': id_dim_emocao, 
                'vlr_confianca': confianca,
                'vlr_resultado': vlr_resultado,
                'data': id_dim_data,
                'hora': hora,
                'guid': guids}
        
        return pd.DataFrame.from_dict(fato)
            
    def fatoSentimento(self):
        df = self.tabelaSentimentos()
        df.to_csv(self.TBL_FAT_SENTIMENTO, index=False ,sep=self.SEP)
