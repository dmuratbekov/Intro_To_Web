# Practical Examples
# 1. Creating a Calendar
import calendar

year = 2026
month = 2
print(calendar.month(year, month))


# 2. Implementing a Timer (Countdown)
import time

def countdown(seconds):
    while seconds:
        print("Time remaining:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown(5)


# 3. Measuring Execution Time
import time

start_time = time.time()

sum(range (1, 1000001))
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution Time: {elapsed_time:.4f} seconds")


# 