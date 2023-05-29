from Imports import *
from main import id_list

db = "logs.db"



def get_database_connection(self):
    con = sqlite3.connect(db)
    return con


class Logs:
    def In(self, ID, TYPE, TIME):
        self.ID = ID
        self.TYPE = TYPE
        self.TIME = TIME

        today = datetime.now()
        ID = str(id_list).join(id_list)
        # self.ids.id_number.text = str(ID)
        TYPE = "in"
        TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
        aaa = ID, TYPE, TIME,
        add_data_stmt = ''' INSERT INTO logs(id_number, type, time) VALUES(?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()

    def log_out(self):
        pass

