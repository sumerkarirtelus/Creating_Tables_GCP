# Version 5
# Data is the exact same but we are just duplicating the data for different timestamps

import csv
import math
import datetime
import pandas as pd

print(" ----- Data Duplicator ----- ")
days = int(input("Please enter the number of days you want this data to be duplicated up to: "))

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

df = pd.read_csv('Duplicate_Montreal_Islands_Stats.csv')

with open('duplicate_data.csv','w',encoding='UTF-8',newline='') as f:

    # Adding a header to the csv file
    header = ['NE_ID', 'SYSTEM_ID', 'NE_NAME', 'INIT_TIME', 'TIME_OFFSET', 'GRAN_PERIOD', 'LOCATION', 'EstabAddAttNbr', 'EstabAddSuccNbr', 'ErabAddFailNbr_CpCcTo', 'ErabAddFailNbr_CpCcFail', 'ErabAddFailNbr_UpGtpFail', 'ErabAddFailNbr_UpMacFail', 'ErabAddFailNbr_UpPdcpFail', 'ErabAddFailNbr_UpRlcFail', 'ErabAddFailNbr_RrcSigFail', 'ErabAddFailNbr_RrcSigTo', 'ErabAddFailNbr_CpBhCacFail', 'ErabAddFailNbr_CpCapaCacFail', 'ErabAddFailNbr_CpQosCacFail', 'ErabAddFailNbr_S1apCuFail', 'ErabAddFailNbr_S1apLinkFail', 'ErabAddFailNbr_S1apSigFail', 'ErabAddFailNbr_CpCcInteraction']
    # Instantiating the writer 
    writer = csv.writer(f)
    # Writing the header to the csv
    writer.writerow(header)

     # initial  date in the timestamps
    base = datetime.datetime.strptime('10/5/2022', '%d/%m/%Y')
    print("base: ",base) 

    # Calculate timestamps for the next 7 days every 15 min
    timestamp_list = [base + datetime.timedelta(minutes=x) for x in range(0,n_min,MIN_INTERVAL)]

    iteration = 0

    with open('Duplicate_Montreal_Islands_Stats.csv', mode='r') as reference_file:

        # Looping through the different NEIDs and their respective means and std devs
        for index, row in df.iterrows():

            NEID_df = row['NE_ID']
            System_ID_df = row['SYSTEM_ID']
            NE_NAME_df = row['NE_NAME']
            LOCATION_df = row['LOCATION']

            print(NEID_df)

            # Reading data from csv and assigning it to the variables
            EstabAddAttNbr = row['count(EstabAddAttNbr(count))']
            
            EstabAddSuccNbr = row['count(EstabAddSuccNbr(count))']
           
            ErabAddFailNbr_CpCcTo = row['count(ErabAddFailNbr_CpCcTo(count))']
           
            ErabAddFailNbr_CpCcFail = row['count(ErabAddFailNbr_CpCcFail(count)']
          
            ErabAddFailNbr_UpGtpFail = row['count(ErabAddFailNbr_UpGtpFail(count))']
           
            ErabAddFailNbr_UpMacFail = row['count(ErabAddFailNbr_UpMacFail(count))']
         
            ErabAddFailNbr_UpPdcpFail = row['count(ErabAddFailNbr_UpPdcpFail(count))']
            
            ErabAddFailNbr_UpRlcFail = row['count(ErabAddFailNbr_UpRlcFail(count))']
           
            ErabAddFailNbr_RrcSigFail = row['count(ErabAddFailNbr_RrcSigFail(count))']
            
            ErabAddFailNbr_RrcSigTo = row['count(ErabAddFailNbr_RrcSigTo(count))']
            
            ErabAddFailNbr_CpBhCacFail = row['count(ErabAddFailNbr_CpBhCacFail(count))']
           
            ErabAddFailNbr_CpCapaCacFail = row['count(ErabAddFailNbr_CpCapaCacFail(count))']
          
            ErabAddFailNbr_CpQosCacFail = row['count(ErabAddFailNbr_CpQosCacFail(count))']
            
            ErabAddFailNbr_S1apCuFail = row['count(ErabAddFailNbr_S1apCuFail(count))']
       
            ErabAddFailNbr_S1apLinkFail = row['count(ErabAddFailNbr_S1apLinkFail(count))']
          
            ErabAddFailNbr_S1apSigFail = row['count(ErabAddFailNbr_S1apSigFail(count))']
          
            ErabAddFailNbr_CpCcInteraction = row['count(ErabAddFailNbr_CpCcInteraction(count))']
        

            for i in range(days):

                for j in range(T):

                    iteration = iteration + 1
                    print("Iteration: ",iteration)
                
                    csv_row = []

                    INIT_TIME = timestamp_list[i]

                    csv_row.append(NEID_df)
                    csv_row.append(System_ID_df)
                    csv_row.append(NE_NAME_df)
                    csv_row.append(INIT_TIME)
                    csv_row.append(TIME_OFFSET)
                    csv_row.append(GRAN_PERIOD)
                    csv_row.append(LOCATION_df)

                    # KPIs
                    csv_row.append(EstabAddAttNbr)
                    csv_row.append(EstabAddSuccNbr)
                    csv_row.append(ErabAddFailNbr_CpCcTo)
                    csv_row.append(ErabAddFailNbr_CpCcFail)
                    csv_row.append(ErabAddFailNbr_UpGtpFail)
                    csv_row.append(ErabAddFailNbr_UpMacFail)
                    csv_row.append(ErabAddFailNbr_UpPdcpFail)
                    csv_row.append(ErabAddFailNbr_UpRlcFail)
                    csv_row.append(ErabAddFailNbr_RrcSigFail)
                    csv_row.append(ErabAddFailNbr_RrcSigTo)
                    csv_row.append(ErabAddFailNbr_CpBhCacFail)
                    csv_row.append(ErabAddFailNbr_CpCapaCacFail)
                    csv_row.append(ErabAddFailNbr_CpQosCacFail)
                    csv_row.append(ErabAddFailNbr_S1apCuFail)
                    csv_row.append(ErabAddFailNbr_S1apLinkFail)
                    csv_row.append(ErabAddFailNbr_S1apSigFail)
                    csv_row.append(ErabAddFailNbr_CpCcInteraction)

                    # Writing to csv file
                    # csv_row is the array where the data will be written to before the entire row is appended to the csv
                    writer.writerow(csv_row)

                    
