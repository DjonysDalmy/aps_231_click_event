import sqlite3

from repository.RegisterRepository import RegisterRepository
from enumeration.Messages import Messages
from entity.Register import Register
class RegisterService:

    def __init__(self):
        self.register_repository = RegisterRepository()
        self.register_repository.set_up_register_repository()

    def create_register(self, user_id, event_id):
        register = Register(None, user_id, event_id, False, None)
        try:
            self.register_repository.insert_register(register.get_id(), register.get_user_id(), register.get_event_id(), register.get_checkin_done(), register.get_checkin_timestamp())
            return Messages.REGISTER_INSERT_OK.value
        except:
            return Messages.OPS.value

    def delete_register(self, user_id, event_id):
        try:
            self.register_repository.delete_register(user_id, event_id)
            return Messages.REGISTER_REMOVE_OK.value
        except:
            return Messages.OPS.value

    def check_register(self, user_id, event_id):
        from_repository_register = self.register_repository.check_register(user_id, event_id)
        return from_repository_register == None
    
    def get_registers(self, event_id):
        from_db_register = self.register_repository.check_registers(event_id)
        registers = []
        for register in from_db_register:
            registers.append(Register.from_database(register))
        return registers
    
    def update_checkin(self, user_id, event_id):
        self.register_repository.update_register(user_id, event_id)
