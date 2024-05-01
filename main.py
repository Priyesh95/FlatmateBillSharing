from flat import Bill
from flat import Flatmate
from reports import PdfReport

amount = float(input("Please enter the bill amount: "))
period = input("What is the period? eg. December 2020 ")

name1 = input("Please enter your name? ")
num_of_days1 = int(input(f"How many days {name1} stay during the period? "))

name2 = input("Please enter your name? ")
num_of_days2 = int(input(f"How many days {name2} stay during the period? "))


bill = Bill(amount,period)
John = Flatmate(name1,num_of_days1)
Mary = Flatmate(name2,num_of_days2)
report = PdfReport(period)
print(John.pays(bill,Mary))
print(Mary.pays(bill,Mary))

report.generate(John, Mary, bill)

