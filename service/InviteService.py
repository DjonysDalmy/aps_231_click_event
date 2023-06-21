import sqlite3

from enumeration.Messages import Messages
from repository.InviteRepository import InviteRepository

class InviteService:

    def __init__(self):
        self.invites_repository = InviteRepository()
        self.invites_repository.set_up_invites_repository()

    def send_invites(self, event_id, users_mail_and_id, timestamp):
        duplicated_invites = self.validate_duplication(event_id, users_mail_and_id)
        if (len(duplicated_invites) != 0):
            message = Messages.INVITE_DUPLICATED.value
            for mail in duplicated_invites:
                message = message + mail
                if duplicated_invites.index(mail) + 1 != len(duplicated_invites):
                    message = message + ", "
            return message
        
        for user_mail_id in users_mail_and_id:
            self.invites_repository.save_invite(event_id, user_mail_id[0], timestamp)
        return Messages.INVITES_OK.value
            
    def validate_duplication(self, event_id, users_mail_and_id):
        duplicated_invites = []
        for user_mail_id in users_mail_and_id:
            if len(self.invites_repository.get_invite_by_user_and_event(event_id, user_mail_id[0])) != 0:
                duplicated_invites.append(user_mail_id[1])
        return duplicated_invites