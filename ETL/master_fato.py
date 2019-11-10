import fat_genero as genero
import fat_sentimento as sentimento
import fat_pessoa as pessoa
import fat_cartaz as cartaz
import conexao
from datetime import datetime


def masterFato():
    # fato gênero
    print('[INFO] criando a fato de gênero')
    gn = genero.Genero()
    df_gn = gn.fatoGenero()
    print('[INFO] fato de gênero criada!')
    
    # fato sentimento
    print('[INFO] criando a fato de sentimento')
    sn = sentimento.Sentimento()
    Sdf_sn = sn.fatoSentimento()
    print('[INFO] fato de sentimento criada!')
    
    # fato pessoa
    print('[INFO] criando a fato pessoa')
    ps = pessoa.Pessoa()
    df_ps = ps.fatoPessoa()
    print('[INFO] fato de pessoa criada!')
    
    # fato cartaz
    print('[INFO] criando a fato cartaz')
    ct = cartaz.Cartaz()
    df_ct = ct.fatoCartaz()
    print('[INFO] fato cartaz criada!')
