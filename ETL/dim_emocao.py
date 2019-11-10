import conexao
import numpy as np
import pandas as pd

class Emocao:
    
    CAMINHO_DB = '../DB/dim'
    DB_NOME = 'dim_emocao'
    EXTENS_DB = '.csv'
    SEP = ';'
    
    TBL_DIM_EMOCAO = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def tabelaEmocoes(self):
        emocoes = []
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'sentimentos':
                            for item_chave, item_valor in atributo.items():
                                emocoes.append(item_chave)
                                
        emocoes_distinct = np.unique(np.array(emocoes))
        ids = [i + 1 for i in range(0, len(emocoes_distinct))]
        
        dimensao = {'id_emocao': ids, 'descricao_emocao': emocoes_distinct}
        
        return pd.DataFrame.from_dict(dimensao)
    
    def dimensaoEmocao(self):
        df = self.tabelaEmocoes()
        df.to_csv(self.TBL_DIM_EMOCAO, index=False ,sep=self.SEP)
