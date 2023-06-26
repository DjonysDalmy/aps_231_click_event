import sqlite3

class EvaluationRepository:

    def set_up_evaluation_repository(self):
        self.conn = sqlite3.connect('event_click.db')

        def trace_callback(query):
            print(query)

        self.conn.set_trace_callback(trace_callback)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS evaluations
                (id TEXT PRIMARY KEY, user_id TEXT, event_id TEXT, rate INTEGER, comment TEXT, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(event_id) REFERENCES events(id))''')

    def insert_evaluation(self, id, user_id, event_id, rate, comment):
        self.c.execute("INSERT INTO evaluations VALUES (?,?,?,?,?)", (id, user_id, event_id,  rate, comment))
        self.conn.commit()
    