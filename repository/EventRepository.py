import sqlite3

class EventRepository:

    def set_up_events_repository(self):
        # criação do banco de dados e tabela para usuários
        self.conn = sqlite3.connect('event_click.db')
        self.c = self.conn.cursor()
        #c.execute('''DROP TABLE events''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS events
                (id TEXT PRIMARY KEY, title TEXT, description TEXT, location TEXT, date DATE, time TEXT, visibility INTEGER NOT NULL, organizer TEXT, FOREIGN KEY(organizer) REFERENCES users(id))''')
        
    def create_or_update_event(self, event):
        self.c.execute("INSERT OR REPLACE INTO events (id, title, description, location, date, time, visibility, organizer) VALUES (?,?,?,?,?,?,?,?)", (event.get_id(), event.get_titulo(), event.get_descricao(), event.get_local(), event.get_data(), event.get_horario(), event.get_visibilidade().value, event.get_organizador().get_id()))
        self.conn.commit()
        
    def select_event(self, event_id):
        self.c.execute("SELECT * FROM events WHERE id=?", (event_id,))
        return self.c.fetchone()
    
    def get_all_events_by_organizer(self, user_id):
        self.c.execute("SELECT * FROM events WHERE organizer=?", (user_id,))
        return self.c.fetchall()
    
    def delete_event(self, event_id):
        self.c.execute("DELETE FROM events WHERE id =?", (str(event_id),))
        self.conn.commit()

    def get_all_public_events(self, user_id):
        self.c.execute("SELECT * FROM events WHERE organizer != ? AND visibility = 0", (user_id,))
        return self.c.fetchall()
    
    def get_public_events_by_date(self, date, user_id):
        self.c.execute("SELECT * FROM events WHERE organizer != ? AND date = ? AND visibility = 0", (user_id, date,))
        return self.c.fetchall()
    
    def get_public_events_by_location(self, location, user_id):
        self.c.execute("SELECT * FROM events WHERE organizer != ? AND location = ? AND visibility = 0", (user_id, location,))
        return self.c.fetchall()
    
    def get_public_events_by_location_and_date(self, location, date, user_id):
        self.c.execute("SELECT * FROM events WHERE organizer != ? AND location = ? AND date = ? AND visibility = 0", (user_id, location, date,))
        return self.c.fetchall()
    