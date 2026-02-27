# Working with the datetime Module
from datetime import datetime

# Example: Getting the Current Date and Time
current_time = datetime.now()
print("Current date and time:", current_time)


# Example: Extracting Date Components
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)


# Example: Creating a Specific Date and Time
specific_date = datetime(2026, 2, 10, 12, 5, 0)
print("Specific Date:", specific_date)


# Example: Formatting a Date
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formate Date:", formatted_date)


# Example: Converting a String to a Date Object
date_str = "01-02-2025 14:30:45"
date_obj = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print("Parsed Date Object:", date_obj)


# Example: Adding and Subtracting Days
from datetime import timedelta

future_date = current_time + timedelta(days=7)
print("Future Date:", future_date)

past_date = current_time - timedelta(days=3)
print("Past Date:", past_date)


# Example: Days Until a Future Event
event_date = datetime(2025, 12, 31)
days_remaining = event_date - current_time
print("Days until event:", days_remaining.days)

