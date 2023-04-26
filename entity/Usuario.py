import uuid

class Usuario:
    
    def __init__(self, id, nome, email, senha, is_organizer):
        self._nome = nome
        self._email = email
        self._senha = senha
        if id == None:
            self._id = str(uuid.uuid4())
        else:
            self._id = id
        self._is_organizer = is_organizer
        
    def get_id(self):
        return self._id
        
    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome
        
    def get_email(self):
        return self._email 
    
    def set_email(self, novo_email):
        self._email = novo_email
        
    def get_senha(self):
        return self._senha
    
    def set_senha(self, nova_senha):
        self._senha = nova_senha
        
    def get_is_organizador(self):
        return self._is_organizer
        
    def set_is_organizador(self, is_organizer):
        self._is_organizer = is_organizer
        
        