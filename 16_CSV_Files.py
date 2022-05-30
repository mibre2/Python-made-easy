# csv = Comma Seperated Values
    # csv is a text value that contains data seperated by commas.
# Note: Due to csv being text files, everything is a string even if you consider it otherwise.
    # When reading a csv it is up to you to convert everything to the proper data type.

# This tutorial will use "16.1_google_stock_data.csv" to:
    # Read and write to a csv
    # How to use the python CSV module by:

import csv
from datetime import datetime

#===============================

path = "[YOUR PATH GOES HERE]\\Python-made-easy\\16.1_google_stock_data.csv"   # Path of your csv file goes here
file = open(path, newline='')
reader = csv.reader(file)

#===============================

header = next(reader) # The "next" function extracts that line of data. You want to do this because typically the first line contains no data and is just a label. 

#===============================

# Convert data to appropriate types.

data = [] 
for row in reader:
    # row = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj. Close']
    date = datetime.strptime(row[0], '%m/%d/%Y')    # First argument is the string, whereas the second is the expected format
    open_price = float(row[1])  # 'open' is a builtin function. Use the help function for more information one why it's called 'open_price' instead.
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

# Display the data as dates, floats, and ints.
print(data[0])

#===============================

# Compute and store daily stock returns 
# And write them to a seperate csv 

# Stock Return = % change in price 
    # Look here for more info: https://www.investopedia.com/terms/r/return.asp
    # Common Time frames:
        # Daily
        # Weekly
        # Monthly
        # Quarterly 


returns_path = "[YOUR PATH GOES HERE]\\Python-made-easy\\16.2_google_returns.csv"   # Path of your return csv file goes here
file = open(returns_path, "w")
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data)-1): 
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]

    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([todays_date, daily_return])
    writer.writerow([formatted_date, daily_return])
