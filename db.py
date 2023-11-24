import sqlite3
class DatabaseManager():
    def __init__(self, path):
        self.conn=sqlite3.connect(path)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur=self.conn.cursor()

    def query(self,arg,values=None):
        if values==None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def create_tables(self):
        self.query('''CREATE TABLE IF NOT EXISTS Users(email text, name text,lastname text)''')

    def fetchone(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()