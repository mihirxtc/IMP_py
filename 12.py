# 12. Write a program to import detetime module and format the date as required. Also use the same module to calculate the difference between your birthday and today in days.

import datetime as dt

current_date = dt.datetime.now()

print("Formated date:",current_date.strftime("%d-%m-%Y"))

a = int(input("Enter ur birth-date: "))
b = int(input("Enter ur birth-month: "))
c = int(input("Enter ur birth-year: "))

birthday = dt.datetime(c,b,a)

difference = current_date - birthday
difference = difference.days
print(difference)