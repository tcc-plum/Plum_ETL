import master_dimensao as dim
import master_fato as fat
import time

def ETL():
    #dim.masterDimensao()
    fat.masterFato()

while True:
    erro = False
    
    try:
        ETL()
    except:
        print('[ERRO] Não foi possível gerar os ETL')
        erro = True
    
    if not erro:
        time.sleep(3)
    