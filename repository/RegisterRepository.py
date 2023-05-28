import sqlite3

class RegisterRepository:

    def set_up_register_repository(self):
        # criação do banco de dados e tabela para a relação Usuario -> Evento
        self.conn = sqlite3.connect('event_click.db')

        def trace_callback(query):
            print(query)

        self.conn.set_trace_callback(trace_callback)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS register
                (id TEXT PRIMARY KEY, user_id TEXT, event_id TEXT, checkin_done INTEGER, checkin_timestamp DATE, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(event_id) REFERENCES events(id))''')

    def insert_register(self, id, user_id, event_id, checkin_done, checkin_timestamp):
        self.c.execute("INSERT INTO register VALUES (?,?,?,?,?)", (id, user_id, event_id, checkin_done, checkin_timestamp))
        self.conn.commit()

    def delete_register(self, user_id, event_id):
        self.c.execute("DELETE FROM register WHERE event_id =? and user_id =?", (str(event_id),str(user_id)))
        self.conn.commit()

    def check_register(self, user_id, event_id):
        self.c.execute("SELECT * FROM register WHERE event_id =? and user_id =?", (str(event_id),str(user_id)))
        return self.c.fetchone()