# Version 6
# We take data for 1 day and duplicate it over x amount of days

import csv
import math
import datetime
import pandas as pd

# Getting user input

print(" ----- Data Duplicator ----- ")
days = int(input("Please enter the number of days you want this data to be duplicated up to: "))

df = pd.read_csv('Duplicate_Montreal_Islands_Stats.csv')

# Time constants
T = 96
MIN_PER_DAY = 1440 # capital letters indicate a constant in my naming convention.
MIN_INTERVAL = 15  # Time interval between samples in minutes. 15 for Samsung and 30 for Huawei.

# Let's generate timestamps for 1 day
n_min = days * MIN_PER_DAY
# to add more days multiply MIN_PER_DAY by the desired nbr of days.

# inputs (avg_val, std_dev, t(48 or 96), T(total number of days))

TIME_OFFSET = "+00:00"
GRAN_PERIOD = MIN_INTERVAL

with open('duplicate_data_v2.csv','w',encoding='UTF-8',newline='') as file_write:

    # headers of the file
    data_columns = list(df.columns)

    # Instantiate the writer
    writer = csv.writer(file_write)

    # Write the header to the file
    writer.writerow(data_columns)

    # initial  date in the timestamps
    base = datetime.datetime.strptime('10/5/2022', '%d/%m/%Y')
    print("base: ",base) 

    # Calculate timestamps for the next 7 days every 15 min
    timestamp_list = [base + datetime.timedelta(minutes=x) for x in range(0,n_min,MIN_INTERVAL)]

    for i in range(days):

        for index, row in df.iterrows(): 

            row_value = []

            for k in range(len(data_columns)):

                cell_val = row[data_columns[k]]
                print(cell_val)

                row_value.append(cell_val)
        
            writer.writerow(cell_val)

