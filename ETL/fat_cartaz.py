import conexao
import numpy as np
import pandas as pd
from datetime import datetime

class Cartaz:
    
    CAMINHO_DB = '../DB/fat'
    DB_NOME = 'fat_cartaz'
    EXTENS_DB = '.csv'
    SEP = ';'
    TBL_FAT_CARTAZ = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def trataCartazNome(self, nome):
        nome_resultado = nome.split('_')
        return nome_resultado[-3]+ ' ' + str(nome_resultado[-2])
        
    def pesquisaID(self, nome, dimensao):
        for indice in dimensao:
            if indice[1] == nome:
                return indice[0]

    def tabelaCartazes(self):
        # inicializa variaveis
        hora = []
        id_dim_cartaz = []
        id_dim_data = []
        guids = []
        
        # carrega dimensões
        dim_cartaz = conexao.Conexao().carregaDimensao('../DB/dim/dim_cartaz.csv')

        # carrega os dados da fato
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'foto':
                            for item_chave, item_valor in atributo.items():
                                if item_chave == 'url':
                                    nome_cartaz = self.trataCartazNome(item_valor)
                                    cartaz = self.pesquisaID(nome_cartaz, dim_cartaz)
                                    id_dim_cartaz.append(cartaz)
                                    guids.append(chave)
                        if item == 'data':
                            id_data = datetime.strptime(atributo, '%Y-%m-%d %H:%M:%S.%f').date()
                            hora_data = datetime.strptime(atributo, '%Y-%m-%d %H:%M:%S.%f').time()
                            id_dim_data.append(id_data)
                            hora.append(hora_data)

        ids = [i + 1 for i in range(0, len(guids))]
        
        fato = {'id_fato_cartaz': ids, 
                'id_cartaz': id_dim_cartaz,
                'data': id_dim_data,
                'hora': hora,
                'guid': guids}
        
        return pd.DataFrame.from_dict(fato)
    
    def fatoCartaz(self):
        df = self.tabelaCartazes()
        df.to_csv(self.TBL_FAT_CARTAZ, index=False ,sep=self.SEP)
