import uuid


class Register:

    def __init__(self, id, user_id, event_id, checkin_done, checkin_timestamp):
        self._user_id = user_id
        self._event_id = event_id
        self._checkin_done = checkin_done
        self._checkin_timestamp = checkin_timestamp

        if id == None:
            self._id = str(uuid.uuid4())
        else:
            self._id = id

    @classmethod    
    def from_database(cls, fromDatabaseObject):
        return Register(fromDatabaseObject[0], fromDatabaseObject[1], fromDatabaseObject[2], fromDatabaseObject[3], fromDatabaseObject[4])
        
    def get_id(self):
        return self._id

    def get_user_id(self):
        return self._user_id

    def get_event_id(self):
        return self._event_id

    def get_checkin_done(self):
        return self._checkin_done

    def set_checkin_done(self, checkin_done):
        self._checkin_done = checkin_done

    def get_checkin_timestamp(self):
        return self._checkin_timestamp

    def set_checkin_timestamp(self, checkin_timestamp):
        self._checkin_timestamp = checkin_timestamp


