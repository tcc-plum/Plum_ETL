import pyrebase
import pandas as pd

class Conexao:
    
    FIREBASE_KEY = "AIzaSyBYZqhEllq8-vN0XN_yBpav54CCVGRHq9E"
    FIREBASE_AUTH = "teste-tcc-2c7b3.firebaseapp.com"
    FIREBASE_DATABASE = "https://teste-tcc-2c7b3.firebaseio.com/"
    FIREBASE_STORAGE = "teste-tcc-2c7b3.appspot.com"
    
    def firebase(self):
        k_fields = ["apiKey", "authDomain", "databaseURL", "storageBucket"]
        v_fields = [self.FIREBASE_KEY, self.FIREBASE_AUTH, self.FIREBASE_DATABASE, self.FIREBASE_STORAGE]
        config = dict(zip(k_fields, v_fields))
        return pyrebase.initialize_app(config)
    
    def storage(self):
        return self.firebase().storage()
    
    def database(self):
        return self.firebase().database()
    
    def dados(self):
        return dict(self.database().child("sky").get().val())
    
    # def GUID(self):
    #     return [chave for chave, valor in self.dados().items()]
    
    def carregaDimensao(self, caminho, delimitador=';'):
        return pd.read_csv(caminho, delimiter=delimitador).values.tolist()