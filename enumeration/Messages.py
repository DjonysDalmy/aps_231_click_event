from enum import Enum

class Messages(Enum):
    LOGIN_ERROR = 'E-mail ou senha incorretos'
    LOGIN_OK = 'Login realizado com sucesso!'
    
    USER_INSERT_OK = 'Usuário cadastrado com sucesso!'
    USER_DUPLICATED_EMAIL = 'E-mail já cadastrado. Por favor, faça o login ou cadastre uma nova pessoa.'
    USER_NOT_FOUND = 'Nenhum usuario encontrado com o e-mail '
    
    SQL_LITE_INTERFACE_ERROR = 'Erro na conexão com o banco de dados. Tente novamente mais tarde.'
    
    EVENT_INSERT_OR_UPDATE_OK = 'Evento cadastrado ou atualizado com sucesso!'
    EVENT_DELETE_OK = 'Evento removido com sucesso!'

    INVITES_OK = 'Usuários convidados com sucesso!'
    INVITE_DUPLICATED = 'Os seguintes e-mails já foram convidados para o evento: '

    REGISTER_INSERT_OK = 'Registro feito com sucesso!'
    REGISTER_REMOVE_OK = 'Registro cancelado com sucesso!'
    RATING_SUBMIT_OK = 'Avaliação submetida com sucesso!'
    OPS = 'Parece que algo deu errado, tente novamente mais tarde!'
