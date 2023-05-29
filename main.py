import datetime

from kivy.uix.boxlayout import BoxLayout

from Imports import *
from Messages import Send_Message
from cloud import Cloud_Update





id_list = []
status = []
update_date = []
Hours = []
sammm = ["sam weiss", "duvy weiss", "adle weiss"]
payment_hours = []


db = "logs.db"


def get_database_connection():
    con = sqlite3.connect(db)
    return con


class MainWidget(Screen):
    def get_info(self):
        update_date.clear()
        print("['SYSTEM IS GETTING YOUR ID NUMBER'....]")
        id_list.clear()
        status.clear()
        NUMBER = self.ids.card_nn.text
        id_list.append(NUMBER)
        print(f"['THIS IS WHATS THE SYSTEM GOT YOUR ID AS'... {id_list}")
        sql_query = ''' SELECT date FROM cloud_logs ORDER BY date DESC LIMIT 1;'''
        con = get_database_connection()
        cur = con.cursor()
        cur.execute(sql_query)
        results_type = cur.fetchall()
        update_date.append(results_type)
        print(f"this is the last update date {update_date}")
        con.commit()
        con.close()

    def Login_statuss(self):
        print("welcome to 'Login Status'")
        id_n = str(id_list).join(id_list)
        format_id  = id_n
        print(f"['THIS IS THE NEW Format ID']  {format_id}")

        if not len(id_n) < 1:
            if True:
                Hours.clear()
                sql_query_fname = ''' SELECT fname FROM info WHERE id=?; '''
                sql_query_lname = ''' SELECT lname FROM info WHERE id=?; '''
                sql_query_type = ''' SELECT type FROM info WHERE id=?; '''
                sql_query_hours = ''' SELECT time FROM logs WHERE id_NUMBER=? AND type=? ORDER BY time DESC LIMIT 1; '''
                con = get_database_connection()
                cur = con.cursor()

                # name
                cur.execute(sql_query_fname, [format_id])
                print(f" ['THIS IS THE NEW Format ID'] {format_id}")
                results_fname = cur.fetchall()
                # phone
                cur.execute(sql_query_lname, [format_id])
                results_lname = cur.fetchall()
                # type
                cur.execute(sql_query_type, [format_id])
                results_type = cur.fetchall()

                # Hours
                typee = "in"
                cur.execute(sql_query_hours, [format_id, typee])
                results_hours = cur.fetchall()
                Hours.append(results_hours)
                print(f"this is results hours {results_hours}")
                print(f"this is Hours list {Hours}")

                con.commit()
                con.close()
                print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR FIRST NAME'] {results_fname}")
                print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR LAST NAME'] {results_lname}")
                print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR TYPE'] {results_type}")

                if results_type == [('admin',)]:
                    print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR STARTING ID...']] {id_list}")
                    id_n = str(id_list).join(id_list)
                    print(f" ['THIS IS WHAT THE SYSTEM GOT FOR YOUR ID... '] {id_n}")
                    add_data_stmt = "SELECT type FROM logs WHERE id_number=? ORDER BY rowid DESC LIMIT 1;"
                    con = get_database_connection()
                    cur = con.cursor()
                    cur.execute(add_data_stmt, [id_n])
                    results = cur.fetchall()
                    print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR RESULT'] {results}")
                    print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR STARTING STATUS... ']{status}")
                    status.clear()
                    status.append(results)
                    con.commit()
                    con.close()

                elif results_type == [('user',)]:
                    print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR STARTING ID...']] {id_list}")
                    id_n = str(id_list).join(id_list)
                    print(f" ['THIS IS WHAT THE SYSTEM GOT FOR YOUR ID... '] {id_n}")
                    add_data_stmt = "SELECT type FROM logs WHERE id_number=? ORDER BY rowid DESC LIMIT 1;"
                    con = get_database_connection()
                    cur = con.cursor()
                    cur.execute(add_data_stmt, [id_n])
                    results = cur.fetchall()
                    print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR RESULT'] {results}")
                    print(f"['THIS IS WHAT THE SYSTEM GOT FOR YOUR STARTING STATUS... ']{status}")
                    status.clear()
                    status.append(results)
                    con.commit()
                    con.close()
                else:
                    print(""""No User Found Under This ID
    Please Contact The Admin """)


class Login(Screen):

    def Back_home(self):
        id_list.clear()
        self.ids.sent_con.text = ""
        self.ids.payment_input.text = ""

    def In(self):
        today = datetime.now()
        ID = str(id_list).join(id_list)
        TYPE = "in"
        TIME = today.strftime("%m/%d/%Y, %I:%M %p")
        tIME = today.strftime("%m/%d/%Y, %H:%M:%S")
        blank = ""
        aaa = ID, TYPE, tIME, blank
        add_data_stmt = ''' INSERT INTO logs(id_number, type, time, sub) VALUES(?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()
        if self.ids.my_toggle_button.text == "Send Login Message Is Set To ON":
            try:
                Send_Message.Message_bot(self, ID=ID, TYPE=TYPE, TIME=TIME, SUBB=False)
                #print("['THE SYSTEM IS RUNNING A CLOUD UPDATE'.....]")
                # Cloud_Update.cloud_update(self)
                #print("['THE SYSTEM IS DONE WITH THE CLOUD UPDATE'.....]")
            except:
                print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
            else:
                print("Email Sent Successfully")
        else:
            pass




    def Out(self):
        date_format = '%m/%d/%Y, %H:%M:%S'
        hrs = "".join(str(x)for t in Hours for x in t)
        val = hrs
        print(f"this val {val}")
        new_hrs = hrs.strip('()')  # remove parentheses
        vall = new_hrs[1:-2]
        print(f"this is new hhr   {vall}")
        today = datetime.now()
        ttd = today.strftime("%m/%d/%Y, %H:%M:%S")

        start_datetime = datetime.strptime(vall, date_format)
        end_datetime = datetime.strptime(ttd, date_format)

        time_difference = end_datetime - start_datetime
        hourss = time_difference.total_seconds() / 3600

        print(f"this is hourss {hourss}")

        subb = str(time_difference)

        print(f"this is  sub hrs worked  {time_difference}")

        ID = str(id_list).join(id_list)
        TYPE = "out"
        TIME = today.strftime("%m/%d/%Y, %I:%M %p")
        aaa = ID, TYPE, TIME, hourss
        add_data_stmt = ''' INSERT INTO logs(id_number, type, time, sub) VALUES(?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()
        if self.ids.my_toggle_button.text == "Send Login Message Is Set To ON":
            try:
                Send_Message.Message_bot(self, ID=ID, TYPE=TYPE, TIME=TIME, SUBB=hourss)
                # print("['THE SYSTEM IS RUNNING A CLOUD UPDATE'.....]")
                # Cloud_Update.cloud_update(self)
                # print("['THE SYSTEM IS DONE WITH THE CLOUD UPDATE'.....]")
            except:
                print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
            else:
                print("Email Sent Successfully")
        else:
            pass

    def Dis_status(self):
        today = datetime.now()
        print("welcome to 'Dis_status' ")
        print(f"['THE SYSTEM IS GETTING YOUR STATUS AS....'] {status}")
        format_status = str(status)
        # self.ids.clocked_status.text = str(kkk)
        self.ids.update_date.text = str(update_date)

        print(f"['PRINTING YOUR FORMATTED_STATUS AS'....]{format_status}")
        if format_status == "[[('out',)]]":
            self.ids.clocked_status.text = str("Out")
            print(f"got a {format_status} answer")
            TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
            self.ids.date_label.text = str(TIME)
        elif format_status == "[[('in',)]]":
            self.ids.clocked_status.text = str("In")
            print(f"got a {format_status} answer")
            TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
            self.ids.date_label.text = str(TIME)

        elif format_status == "[[]]":
            self.ids.clocked_status.text = str("Out")
            print(f"got a {format_status} answer")
            TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
            self.ids.date_label.text = str(TIME)

        else:
            self.ids.clocked_status.text = str("No Data Found For This User")
            print(f"No Data Found For This User: {format_status}")
            print("i got nothing")
            TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
            self.ids.date_label.text = str(TIME)

    def Cloud_update_screen(self):
        pass

    def Payments(self):
        payment_hours.clear()
        print("welcome to 'payments'")
        id_n = str(id_list).join(id_list)
        format_id = id_n
        print(f"['THIS IS THE NEW Format ID']  {format_id}")
        print(f"this is ID {format_id}")
        print("['SYSTEM IS STARTING PAYMENTS....']")
        today = datetime.now()
        sql_query = ''' SELECT amount_w FROM payments WHERE id_number=? ORDER BY date DESC LIMIT 1;'''
        con = get_database_connection()
        cur = con.cursor()
        cur.execute(sql_query, [format_id])
        results_amount_w = cur.fetchall()
        print(f"this is the totel of hours {results_amount_w}")
        con.commit()
        con.close()



        ID = str(id_list).join(id_list)
        TIME = today.strftime("%m/%d/%Y, %I:%M %p")
        AMOUNT = self.ids.payment_input.text
        aaa = ID, TIME, "N/A", AMOUNT
        add_data_stmt = ''' INSERT INTO payments(id_number, date, amount_w, amount) VALUES(?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()
        if self.ids.my_toggle_button.text == "Send Login Message Is Set To ON":
            try:
                Send_Message.Payment_bot(self, ID=ID, AMOUNT=AMOUNT, TIME=TIME, SUBB="N/A")
                # print("['THE SYSTEM IS RUNNING A CLOUD UPDATE'.....]")
                # Cloud_Update.cloud_update(self)
                # print("['THE SYSTEM IS DONE WITH THE CLOUD UPDATE'.....]")
            except:
                print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
            else:
                print("Email Sent Successfully")
                self.ids.sent_con.text = "Payment Confirmed"
                self.ids.payment_input.text = ""
        else:
            self.ids.sent_con.text = "Payment Confirmed"
            self.ids.payment_input.text = ""


class Cloud_update_page(Screen, BoxLayout, Cloud_Update):

    def Load_bar(self):
        print(f"this is the starting value for the pr bar {self.ids.prbar.value}")
        print("calling the def methud")
        starting_number = .1
        num = ""
        bar_status = self.ids.prbar.value
        print("about to start the loop")
        while bar_status <= 100:
            num = bar_status + starting_number
            bar_status = num
            self.ids.prbar.value = bar_status
        today = datetime.now()
        ID = str(id_list).join(id_list)
        TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
        aaa = ID, TIME
        add_data_stmt = ''' INSERT INTO cloud_logs(user, date) VALUES(?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()
        print(f"THIS IS THE ENDING PR BAR LEVEL NUMBER..... {self.ids.prbar.value}")
        Cloud_Update.cloud_update(self)
        self.ids.prmessage.text = "Done With The Cloud Update"



    def pay_update(self):
        print(f"this is the starting value for the pr bar {self.ids.prbar.value}")
        print("calling the def methud")
        starting_number = .1
        num = ""
        bar_status = self.ids.prbar.value
        print("about to start the loop")
        while bar_status <= 100:
            num = bar_status + starting_number
            bar_status = num
            self.ids.prbar.value = bar_status
        today = datetime.now()
        ID = str(id_list).join(id_list)
        TIME = today.strftime("%m/%d/%Y, %H:%M:%S")
        aaa = ID, TIME
        add_data_stmt = ''' INSERT INTO cloud_logs(user, date) VALUES(?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()
        print(f"THIS IS THE ENDING PR BAR LEVEL NUMBER..... {self.ids.prbar.value}")
        Cloud_Update.payment_update(self)
        self.ids.prmessage.text = "Done With The Payment Update"


    def reaset_bar(self):
        bar_status = 100
        self.ids.prbar.value = bar_status
        time.sleep(.4)
        number = 0.0
        self.ids.prmessage.text = "THE SYSTEM IS RUNNING A CLOUD UPDATE"
        self.ids.prbar.value = number


class Message_Center(Screen):
    def message_bu(self):
        for i in sammm:
            self.ids.togbutton.text = str(i)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        Window.Clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == "__main__":
    MainApp().run()