from Imports import *

dj = "clock_me_database.json"
db = "logs.db"
cloud_data = []
Users = []


class Cloud_Update:
    def get_database_connection(self):
        con = sqlite3.connect(db)
        return con

    def cloud_update(self):
        my_conn = create_engine("sqlite:///" + db)
        import pandas as pd
        try:
            query = 'SELECT * FROM logs'
            df = pd.read_sql(query, my_conn, index_col='id_number')
            print(df)
        except SQLAlchemyError as e:
            print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
        else:
            try:
                gc = pygsheets.authorize(service_account_file=dj)
                sh = gc.open('clock_in_database')
                wk1 = sh[0]
                wk1.clear()
                # wk1.append_table(df, start='A1', end=None, dimension='ROWS', overwrite=False)
                wk1.set_dataframe(df, (1, 1), copy_index=True, extend=True)
            except:
                print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
            else:
                print("Dataframe Created Successfully")


    def payment_update(self):
        my_conn = create_engine("sqlite:///" + db)
        import pandas as pd
        try:
            query = 'SELECT * FROM payments'
            df = pd.read_sql(query, my_conn, index_col='id_number')
            print(df)
        except SQLAlchemyError as e:
            print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
        else:
            try:
                gc = pygsheets.authorize(service_account_file=dj)
                sh = gc.open('clock_in_database')
                wk1 = sh[1]
                wk1.clear()
                # wk1.append_table(df, start='A1', end=None, dimension='ROWS', overwrite=False)
                wk1.set_dataframe(df, (1, 1), copy_index=True, extend=True)
            except:
                print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
            else:
                print("Dataframe Created Successfully")



class Get_Cloud_Data:
    print(cloud_data)


class Get_Users:
    print(Users)