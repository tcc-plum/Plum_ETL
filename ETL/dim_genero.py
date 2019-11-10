import conexao
import numpy as np
import pandas as pd

class Genero:
    
    CAMINHO_DB = '../DB/dim'
    DB_NOME = 'dim_genero'
    EXTENS_DB = '.csv'
    SEP = ';'
    
    TBL_DIM_GENERO = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    dados = conexao.Conexao().dados()
    
    def tabelaGeneros(self):
        generos = []
        for chave, valor in self.dados.items():
            for k, v in valor.items():
                if k == 'resposta':
                    for item, atributo in v.items():
                        if item == 'gênero':
                            for item_chave, item_valor in atributo.items():
                                if item_chave == 'valor':
                                    generos.append(item_valor)
                                
        generos_distinct = np.unique(np.array(generos))
        ids = [i + 1 for i in range(0, len(generos_distinct))]
        
        dimensao = {'id_genero': ids, 'descricao_genero': generos_distinct}
        
        return pd.DataFrame.from_dict(dimensao)
    
    def dimensaoGeneros(self):
        df = self.tabelaGeneros()
        df.to_csv(self.TBL_DIM_GENERO, index=False ,sep=self.SEP)
