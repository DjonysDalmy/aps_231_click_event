import sqlite3

from repository.EventRepository import EventRepository
from enumeration.Visibilidade import Visibilidade
from enumeration.Messages import Messages
from entity.Event import Event


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
            return Messages.SQL_LITE_INTERFACE_ERROR
        
    def select_event(self, event_id):
        from_repository_event = self.events_repository.select_event(event_id)
        return Event.from_database(from_repository_event)
    
    def get_all_events_by_organizer(self, user_id):
        from_database_events = self.events_repository.get_all_events_by_organizer(user_id)
        events = []
        for from_db_event in from_database_events:
            events.append(Event.from_database(from_db_event))
        return events
    
    def delete_event(self, event_id):
        try:
            self.events_repository.delete_event(event_id)
            return Messages.EVENT_DELETE_OK.value
        except:
            return Messages.SQL_LITE_INTERFACE_ERROR.value