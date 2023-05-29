from Imports import *

db = "logs.db"

def get_database_connection():
    con = sqlite3.connect(db)
    return con


class Send_Message:

    def Message_bot(self, ID, TYPE, TIME, SUBB):
        self.ID = ID
        self.TYPE = TYPE
        self.TIME = TIME
        self.SUBB = SUBB
        message_list = []
        """sql_query_email = ''' SELECT number FROM message_con; '''
        con = get_database_connection()
        cur = con.cursor()
        cur.execute(sql_query_email)
        print(f" ['Loading Email's']")
        results_email = cur.fetchall()
        message_list.append(results_email)
        print(f"email list.... {message_list}")
        email = str(message_list).join(message_list)
        format_id = email
        print(f"['THIS IS THE NEW Format email']  {format_id}")"""
        f = open('email_users.txt')
        lines = f.readlines()
        for line in lines:
            if line[-1] == "\n":
                message_list.append(line[:-1])
            else:
                message_list.append(line)
        print(message_list)

        for item in message_list:
            email_sender = 'meatpython@gmail.com'
            password = 'hntviotnybdzxuyj'

            email_receiver = item

            subject = "Hey There"
            body = (f"""
                    ID: {ID}
                    Clocked: {TYPE} 
                    At:  {TIME} 
                    Total Amount Of Hours Worked:  {SUBB}
============================================================
""")

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            print(f"EMAIL WAS SENT TO: {item}")



    def Payment_bot(self, ID, AMOUNT, TIME, SUBB):
        self.ID = ID
        self.AMOUNT = AMOUNT
        self.TIME = TIME
        self.SUBB = SUBB
        message_list = []

        f = open('email_users.txt')
        lines = f.readlines()
        for line in lines:
            if line[-1] == "\n":
                message_list.append(line[:-1])
            else:
                message_list.append(line)
        print(message_list)

        for item in message_list:
            email_sender = 'meatpython@gmail.com'
            password = 'hntviotnybdzxuyj'

            email_receiver = item

            subject = "Payment Receipt"
            body = (f"""
            
                    ************* Payment Receipt *************
                    
                    
                                    ID: {ID}
                                    Got Paid: {AMOUNT} 
                                    At:  {TIME} 
                                    Total Amount Of Hours Worked:  {SUBB}
                                    
                                    
                ============================================================
                """)

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            #print(f"EMAIL WAS SENT TO: {item}")
