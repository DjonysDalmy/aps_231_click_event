from enumeration.Visibilidade import Visibilidade
import uuid

class Event:
    
    def __init__(self, id, titulo, descricao, local, data, horario, visibilidade, organizador):
        self._titulo = titulo
        self._descricao = descricao
        self._data = data
        self._horario = horario
        self._visibilidade = visibilidade
        self._local = local
        if id == None:
            self._id = str(uuid.uuid4())
        else:
            self._id = id
        self._organizador = organizador
        self._participantes = None
        self._avaliacoes = None
        
    @classmethod    
    def from_database(cls, fromDatabaseObject):
        return Event(fromDatabaseObject[0], fromDatabaseObject[1], fromDatabaseObject[2], fromDatabaseObject[3], fromDatabaseObject[4], fromDatabaseObject[5], Visibilidade.get_visibility(fromDatabaseObject[6]), fromDatabaseObject[7])
        
    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def get_data(self):
        return self._data

    def set_data(self, nova_data):
        self._data = nova_data

    def get_horario(self):
        return self._horario

    def set_horario(self, novo_horario):
        self._horario = novo_horario
        
    def get_visibilidade(self):
        return self._visibilidade
        
    def set_visibilidade(self, nova_visibilidade):
        self._visibilidade = nova_visibilidade
        
    def get_local(self):
        return self._local
    
    def set_local(self, novo_local):
        self._local = novo_local

    def get_organizador(self):
        return self._organizador

    def set_organizador(self, novo_organizador):
        self._organizador = novo_organizador

    def get_participantes(self):
        return self._participantes

    def insert_participante(self, novo_participante):
        if self._participantes == None:
            self._participantes = [novo_participante]
        else:
            self._participantes.append(novo_participante)
        
    def get_avaliacoes(self):
        return self._avaliacoes
    
    def insert_avaliacao(self, avaliacao):
        if self._avaliacoes == None:
            self._avaliacoes = [avaliacao]
        else:
            self._avaliacoes.append(avaliacao)
    
        
    
        
   
    