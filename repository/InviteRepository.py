import sqlite3

class InviteRepository:

    def set_up_invites_repository(self):
        # criação do banco de dados e tabela para usuários
        self.conn = sqlite3.connect('event_click.db')
        def trace_callback(query):
            print(query)
        self.conn.set_trace_callback(trace_callback)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS invites
                (event_id, user_id, accepted INTEGER, timestamp TEXT, FOREIGN KEY(event_id) REFERENCES events(id), FOREIGN KEY(user_id) REFERENCES users(id), PRIMARY KEY(event_id, user_id))''')
        
    def save_invite(self, event_id, user_id, timestamp):
        self.c.execute("INSERT INTO invites VALUES (?, ?, NULL, ?)", (event_id, user_id, timestamp))
        self.conn.commit()

    def get_invite_by_user_and_event(self, event_id, user_id):
        self.c.execute("SELECT * FROM invites WHERE event_id = ? AND user_id = ?", (event_id, user_id))
        return self.c.fetchall()
    
    def get_invite_by_user_and_unanswered(self, user_id):
        self.c.execute("SELECT * FROM invites WHERE user_id = ? AND accepted IS NULL", (user_id,))
        return self.c.fetchall()

    def update_invite(self, response, user_id, event_id):
        self.c.execute("UPDATE invites SET accepted = ? WHERE user_id=? AND event_id =?", (response, user_id, event_id))
        self.conn.commit()
