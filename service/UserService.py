import sqlite3
from repository.UserRepository import UserRepository
from entity.Usuario import Usuario
from enumeration.Messages import Messages

class UserService:

    def __init__(self):
        self.users_repository = UserRepository()
        self.users_repository.set_up_users_repository()
        
    def create_user(self, name, email, password, is_organizer):
        user = Usuario(None, name, email, password, is_organizer)
        try:            
            self.users_repository.insert_user(user.get_id(), user.get_nome(), user.get_email(), user.get_senha(), user.get_is_organizador())
            return Messages.USER_INSERT_OK.value
        except sqlite3.IntegrityError:
            return Messages.USER_DUPLICATED_EMAIL.value
        except sqlite3.InterfaceError:
            return Messages.SQL_LITE_INTERFACE_ERROR.value
                    
    def check_login(self, email, password):
        user_from_repository = self.users_repository.get_user_by_email(email)
        if user_from_repository != None:
            user = Usuario(user_from_repository[0], user_from_repository[1], user_from_repository[2], user_from_repository[3], user_from_repository[4])
            if user.get_email() == email and user.get_senha() == password:
                self._logged_user = user
                return Messages.LOGIN_OK.value
        return Messages.LOGIN_ERROR.value
        
    def get_logged_user(self):
        return self._logged_user
    
    def update_user(self, user_id, is_organizer):
        self.users_repository.update_user(user_id, is_organizer)