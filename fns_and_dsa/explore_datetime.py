import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("current date:",current_date)

display_current_datetime()

def calculate_future_date():
    user_days = int(input("Enter the numbers of day: "))
    current_date = datetime.datetime.now()
    future_date = current_date + timedelta(days = user_days)
    future_date = future_date.strftime("%y-%m-%d")
    print("future date:",future_date)

calculate_future_date()
