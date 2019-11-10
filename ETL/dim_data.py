import pandas as pd

class Data:
    
    CAMINHO_DB = '../DB/dim'
    DB_NOME = 'dim_data'
    EXTENS_DB = '.csv'
    SEP = ';'
    
    TBL_DIM_DATA = CAMINHO_DB + '/' + DB_NOME + EXTENS_DB
    
    def tabelaCalendario(self, inicio='1900-01-01', fim='2099-12-31'):
        df = pd.DataFrame({'data': pd.date_range(inicio, fim)})
        df['dia'] = df.data.dt.day
        df['dia_da_semana_nome'] = df.data.dt.weekday_name
        df['dia_da_semana_numero'] = df.data.dt.weekday
        df['semana_do_mes'] = (df.dia - 1) // 7 + 1
        df['semana_do_ano'] = df.data.dt.weekofyear
        df['mes_numero'] = df.data.dt.month
        df['mes_nome'] = df.data.dt.month_name()
        df['bimestre'] = df.mes_numero // 2
        df['trimestre'] = df.data.dt.quarter
        df['semestre'] = (df.trimestre + 1) // 2
        df['ano'] = df.data.dt.year
        df['ano_mes_dia'] = df.ano.astype(str) + df.mes_numero.astype(str) + df.dia.astype(str)
        df['ano_mes'] = df.ano.astype(str) + df.mes_numero.astype(str)
        return df
    
    def dimensaoData(self):
        df = self.tabelaCalendario('2016-01-01', '2025-12-31')
        df.to_csv(self.TBL_DIM_DATA, index=False, sep=self.SEP)
        
    