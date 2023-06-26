import uuid


class Evaluations:

    def __init__(self, id, user_id, event_id, nota, comentario):
        self._user_id = user_id
        self._event_id = event_id
        self._nota = nota
        self._comentario = comentario

        if id == None:
            self._id = str(uuid.uuid4())
        else:
            self._id = id

    @classmethod    
    def from_database(cls, fromDatabaseObject):
        return Evaluations(fromDatabaseObject[0], fromDatabaseObject[1], fromDatabaseObject[2], fromDatabaseObject[3], fromDatabaseObject[4])
        
    def get_id(self):
        return self._id

    def get_user_id(self):
        return self._user_id

    def get_event_id(self):
        return self._event_id

    def get_rate(self):
        return self._nota
    
    def get_comment(self):
        return self._comentario


