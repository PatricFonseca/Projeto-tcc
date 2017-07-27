from django.db import models

class Perfil(object):

    def __init__(self, nome='', email='', telefone='', *args, **kwargs):
        #super(CLASS_NAME, self, nome).__init__(*args, **kwargs)
        self.nome     = nome
        self.email    = email
        self.telefone = telefone

    
