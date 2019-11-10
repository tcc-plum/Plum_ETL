import conexao
import numpy as np
import pandas as pd

class Cartaz:
    
    CAMINHO_DB = '../DB/dim'
    DB_NOME = 'dim_cartaz'
    EXTENS_DB = '.csv'
    SEP = ';'
    
    TBL_DIM_CARTAZ = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def tabelaCartazes(self):
        cartazes = []
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'foto':
                            for item_chave, item_valor in atributo.items():
                                if item_chave == 'url':
                                    cartazes.append(item_valor)
        cartazes_tratados = []                        
        for item in cartazes:
            nome = item.split('_')
            cartazes_tratados.append(nome[-3]+ ' ' + str(nome[-2]))

        cartazes_distinct = np.unique(np.array(cartazes_tratados))
        ids = [i + 1 for i in range(0, len(cartazes_distinct))]
        
        dimensao = {'id_cartaz': ids, 'descricao_cartaz': cartazes_distinct}
        
        return pd.DataFrame.from_dict(dimensao)
    
    def dimensaoCartazes(self):
        df = self.tabelaCartazes()
        df.to_csv(self.TBL_DIM_CARTAZ, index=False ,sep=self.SEP)
