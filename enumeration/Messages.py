from enum import Enum

class Messages(Enum):
    LOGIN_ERROR = 'E-mail ou senha incorretos'
    LOGIN_OK = 'Login realizado com sucesso!'
    
    USER_INSERT_OK = 'Usuário cadastrado com sucesso!'
    USER_DUPLICATED_EMAIL = 'E-mail já cadastrado. Por favor, faça o login ou cadastre uma nova pessoa.'
    
    SQL_LITE_INTERFACE_ERROR = 'Erro na conexão com o banco de dados. Tente novamente mais tarde.'
    
    EVENT_INSERT_OR_UPDATE_OK = 'Evento cadastrado ou atualizado com sucesso!'
    EVENT_DELETE_OK = 'Evento removido com sucesso!'