from datetime import datetime, timedelta

# 1. Get the current day, month, year, hour, minute, and timestamp
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

# Print the current day, month, year, hour, minute, and timestamp
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Timestamp: {timestamp}")

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted date: {formatted_date}")

# 3. Change "5 December, 2019" to a datetime object
date_str = "12/05/2019, 00:00:00"
time_obj = datetime.strptime(date_str, "%m/%d/%Y, %H:%M:%S")
print(f"Changed time string to datetime: {time_obj}")

# 4. Calculate the time difference between now and new year
new_year = datetime(year + 1, 1, 1)
time_diff_new_year = new_year - now
print(f"Time difference between now and new year: {time_diff_new_year}")

# 5. Calculate the time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
time_diff_epoch = now - epoch
print(f"Time difference between 1 January 1970 and now: {time_diff_epoch}")
