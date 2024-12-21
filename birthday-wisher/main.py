import pandas
import datetime as dt
import random
import smtplib


my_email = "python.sumeyye@gmail.com"
password = ""

data = pandas.read_csv("birthdays.csv")

today = dt.datetime.now()

for (index, row) in data.iterrows():
    if row.month == today.month and row.day == today.day:
        random_letter = str(random.randint(1, 3))
        print(random_letter)
        with open("./letter_templates/letter_" + random_letter + ".txt") as file:
            letter = file.read()
            new_letter = letter.replace("[NAME]", row.p_name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row.email,
                                msg=f"Subject:Happy Birthday!\n\n{new_letter}")
