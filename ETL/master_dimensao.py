import dim_data as data
import dim_emocao as emocao
import dim_genero as genero
import dim_cartaz as cartaz

def masterDimensao():
    ## dimensão data
    print('[INFO] criando a dimensão de data')
    dt = data.Data()
    df_data = dt.dimensaoData()
    print('[INFO] dimensão de data criada!')
    
    ## dimensão emocao
    print('[INFO] criando a dimensão emoção')
    em = emocao.Emocao()
    df_em = em.dimensaoEmocao()
    print('[INFO] dimensão emoção criada!')
    
    
    ## dimensao genero
    print('[INFO] criando a dimensão gênero')
    gn = genero.Genero()
    df_gn = gn.dimensaoGeneros()
    print('[INFO] dimensão gênero criada!')
    
    ## dimensão cartaz
    print('[INFO] criando a dimensão cartaz')
    cr = cartaz.Cartaz()
    df_cr = cr.dimensaoCartazes()
    print('[INFO] dimensão cartaz criada!')
