# import Datetime Module
import datetime

# Display datetime.date classes
print(help(datetime.date), "\n")

# Make a date called "anon"
anon = datetime.date(1998, 4, 7)     # Birthdate of Anonymous

# Display anonymous birthdate
print("Anonymous birthdate")
print("-------------------")
print(anon, "\n")

# Access year, month, and day seperately
print("Year: ", anon.year)      # Year
print("Month: ", anon.month)    # Month   
print("Day: ", anon.day, "\n")        # Day 

# Display SpaceX first reused rocket datetime
# March 30, 2017 on 22:27 UTC

# Launch date
launch_date = datetime.date(2017,3, 30) # Only contains date
print("Launch date: ", launch_date)
print("-------------")
print("Year: ", launch_date.year)   # Launch date year
print("Month: ", launch_date.month) # Launch date month
print("Day: ", launch_date.day, "\n")     # Launch date day

# Launch time
launch_time = datetime.time(22, 27, 0)  # Only contains time
print("Launch time: ", launch_time)
print("-------------")
print("Hour: ", launch_time.hour) # Launch time hour           # Launch date hour
print("Minute: ", launch_time.minute)       # Launch date minute
print("Second: ", launch_time.second, "\n") # Launch date second

# Launch datetime
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0) # Contains datetime
print("Launch date time: ", launch_datetime)


# Display current Datetime
# The datetime class has a method called "today()"
now = datetime.datetime.today()
print(now)


'''Moon landing happened on 7/20/1969'''

# Convert string of moonlanding to Datetime
# The datetime class has a method called "strptime()"

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")

# Display moon_landing_datetime
print("Moon landing datetime")
print("---------------------")
print(moon_landing_datetime, "\n")
