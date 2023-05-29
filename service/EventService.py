import sqlite3

from repository.EventRepository import EventRepository
from enumeration.Visibilidade import Visibilidade
from enumeration.Messages import Messages
from entity.Event import Event
from entity.Register import Register
from datetime import datetime


class EventService:

    def __init__(self):
        self.events_repository = EventRepository()
        self.events_repository.set_up_events_repository()
        
    def create_or_update_event(self, id, title, description, location, date, time, visibility, organizer):       
        event = Event(id, title, description, location, date, time, Visibilidade.get_visibility(visibility) , organizer)
        try:
            self.events_repository.create_or_update_event(event)
            return Messages.EVENT_INSERT_OR_UPDATE_OK.value
        except sqlite3.InterfaceError:
            return Messages.SQL_LITE_INTERFACE_ERROR.value
        
    def select_event(self, event_id):
        from_repository_event = self.events_repository.select_event(event_id)
        return Event.from_database(from_repository_event)
    
    def get_all_events_by_organizer(self, user_id):
        from_database_events = self.events_repository.get_all_events_by_organizer(user_id)
        events = []
        for from_db_event in from_database_events:
            events.append(Event.from_database(from_db_event))
        return events
    
    def get_registers(self, event_id):
        from_db_register = self.events_repository.get_register(event_id)
        registers = []
        for register in from_db_register:
            registers.append(Register.from_database(register))
        return registers
    
    def delete_event(self, event_id):
        try:
            self.events_repository.delete_event(event_id)
            return Messages.EVENT_DELETE_OK.value
        except:
            return Messages.SQL_LITE_INTERFACE_ERROR.value
        
    def filter_events(self, location, date, user_id):
        data_atual = str(datetime.today().date())
        if location == '': 
            if date == '':
                from_db_events = self.events_repository.get_all_public_events(user_id, data_atual)
            else:
                from_db_events = self.events_repository.get_public_events_by_date(date, user_id, data_atual)
        elif date == '':
            from_db_events = self.events_repository.get_public_events_by_location(location, user_id, data_atual)
        else:
            from_db_events = self.events_repository.get_public_events_by_location_and_date(location, date, user_id, data_atual)

        events = []
        for from_db_event in from_db_events:
            events.append(Event.from_database(from_db_event))
        return events
