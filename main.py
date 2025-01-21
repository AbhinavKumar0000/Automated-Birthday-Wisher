import datetime as dt
import random
import pandas
import smtplib

my_email = "" #write your email here
password = "" #write your password here


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    n = random.randint(1,3)
    file_path = f"letter_templates/letter_{n}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs =bday_person["email"],
            msg = f"Subject:Happy Birthday\n\n{contents}"
        )


