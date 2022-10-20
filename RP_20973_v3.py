
# Version 2
# Reading data from external csv for the average and standard deviations

import csv
import math
import datetime
import pandas as pd

def KPI_random_val(average_val, std_dev_val, t, T):

    # handling any null inputs
    if(average_val == None):
        average_val = 0.0
    if(std_dev_val == None):
        std_dev_val = 0.0
    
    # Formula
    # add noise to the formula
    y = average_val - average_val * math.sin( 2 * math.pi * t / T) # + noise
    return y


# Inputs
print('\n ------ Length of Table ------ \n')
days = int(input("Please enter the number of days: "))

print('\n ------ Inputs for Table ------ \n')
NE_ID = input("NE_ID: ")
SYSTEM_ID = input("SYSTEM_ID: ")
NE_NAME = input("NE_NAME")
INIT_TIME = input("INIT_TIME: ")
TIME_OFFSET = input("TIME_OFFSET: ")
GRAN_PERIOD = input("GRAN_PERIOD: ")
LOCATION = input("LOCATION: ")

# Time constants
T = 96
MIN_PER_DAY = 1440 # capital letters indicate a constant in my naming convention.
MIN_INTERVAL = 15  # Time interval between samples in minutes. 15 for Samsung and 30 for Huawei.

# Let's generate timestamps for 1 day
n_min = days * MIN_PER_DAY
# to add more days multiply MIN_PER_DAY by the desired nbr of days.

# inputs (avg_val, std_dev, t(48 or 96), T(total number of days))

# Hardcoding SYSTEM_ID values
SYSTEM_ID = 21009
TIME_OFFSET = "+00:00"
GRAN_PERIOD = MIN_INTERVAL

df = pd.read_csv('Montreal_Island_stats.csv')

# Writing to csv

with open('tables_v3.csv', 'w', encoding='UTF8', newline='') as f:

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

    with open('Montreal_Island_stats.csv', mode='r') as reference_file:

        df = pd.read_csv('Montreal_Island_stats.csv')

        # Looping through the different NEIDs and their respective means and std devs
        for index, row in df.iterrows():

            NEID_df = row['NEID']
            print(NEID_df)

            # Reading data from csv and assigning it to the variables
            EstabAddAttNbr_avg = row['avg(EstabAddAttNbr(count))']
            EstabAddAttNbr_std_dev = row['stdev(EstabAddAttNbr(count))']
            EstabAddSuccNbr_avg = row['avg(EstabAddSuccNbr(count))']
            EstabAddSuccNbr_std_dev = row['stdev(EstabAddSuccNbr(count))']
            ErabAddFailNbr_CpCcTo_avg = row['avg(ErabAddFailNbr_CpCcTo(count))']
            ErabAddFailNbr_CpCcTo_std_dev = row['stdev(ErabAddFailNbr_CpCcTo(count))']
            ErabAddFailNbr_CpCcFail_avg = row['avg(ErabAddFailNbr_CpCcFail(count)']
            ErabAddFailNbr_CpCcFail_std_dev = row['stdev(ErabAddFailNbr_CpCcFail(count)']
            ErabAddFailNbr_UpGtpFail_avg = row['avg(ErabAddFailNbr_UpGtpFail(count))']
            ErabAddFailNbr_UpGtpFail_std_dev = row['stdev(ErabAddFailNbr_UpGtpFail(count))']
            ErabAddFailNbr_UpMacFail_avg = row['avg(ErabAddFailNbr_UpMacFail(count))']
            ErabAddFailNbr_UpMacFail_std_dev = row['stdev(ErabAddFailNbr_UpMacFail(count))']
            ErabAddFailNbr_UpPdcpFail_avg = row['avg(ErabAddFailNbr_UpPdcpFail(count))']
            ErabAddFailNbr_UpPdcpFail_std_dev = row['stdev(ErabAddFailNbr_UpPdcpFail(count))']
            ErabAddFailNbr_UpRlcFail_avg = row['avg(ErabAddFailNbr_UpRlcFail(count))']
            ErabAddFailNbr_UpRlcFail_std_dev = row['stdev(ErabAddFailNbr_UpRlcFail(count))']
            ErabAddFailNbr_RrcSigFail_avg = row['avg(ErabAddFailNbr_RrcSigFail(count))']
            ErabAddFailNbr_RrcSigFail_std_dev = row['stdev(ErabAddFailNbr_RrcSigFail(count))']
            ErabAddFailNbr_RrcSigTo_avg = row['avg(ErabAddFailNbr_RrcSigTo(count))']
            ErabAddFailNbr_RrcSigTo_std_dev = row['stdev(ErabAddFailNbr_RrcSigTo(count))']
            ErabAddFailNbr_CpBhCacFail_avg = row['avg(ErabAddFailNbr_CpBhCacFail(count))']
            ErabAddFailNbr_CpBhCacFail_std_dev = row['stdev(ErabAddFailNbr_CpBhCacFail(count))']
            ErabAddFailNbr_CpCapaCacFail_avg = row['avg(ErabAddFailNbr_CpCapaCacFail(count))']
            ErabAddFailNbr_CpCapaCacFail_std_dev = row['stdev(ErabAddFailNbr_CpCapaCacFail(count))']
            ErabAddFailNbr_CpQosCacFail_avg = row['avg(ErabAddFailNbr_CpQosCacFail(count))']
            ErabAddFailNbr_CpQosCacFail_std_dev = row['stdev(ErabAddFailNbr_CpQosCacFail(count))']
            ErabAddFailNbr_S1apCuFail_avg = row['avg(ErabAddFailNbr_S1apCuFail(count))']
            ErabAddFailNbr_S1apCuFail_std_dev = row['stdev(ErabAddFailNbr_S1apCuFail(count))']
            ErabAddFailNbr_S1apLinkFail_avg = row['avg(ErabAddFailNbr_S1apLinkFail(count))']
            ErabAddFailNbr_S1apLinkFail_std_dev = row['stdev(ErabAddFailNbr_S1apLinkFail(count))']
            ErabAddFailNbr_S1apSigFail_avg = row['avg(ErabAddFailNbr_S1apSigFail(count))']
            ErabAddFailNbr_S1apSigFail_std_dev = row['stdev(ErabAddFailNbr_S1apSigFail(count))']
            ErabAddFailNbr_CpCcInteraction_avg = row['avg(ErabAddFailNbr_CpCcInteraction(count))']
            ErabAddFailNbr_CpCcInteraction_std_dev = row['stdev(ErabAddFailNbr_CpCcInteraction(count))']

            # Writing data for j number of days which is inputted by the user
            for j in range(days):

                # Writing data for 46 or 96 data samples, depending on the vendor
                for i in range(T):

                    #Writing data to the csv file
                    csv_row = []

                    # NEID
                    NE_ID = NEID_df
                    # EstabAddAttNbr
                    EstabAddAttNbr = KPI_random_val( EstabAddAttNbr_avg, EstabAddAttNbr_std_dev, i, T)
                    # EstabAddSuccNbr
                    EstabAddSuccNbr = KPI_random_val( EstabAddSuccNbr_avg, EstabAddSuccNbr_std_dev, i, T)
                    # ErabAddFailNbr_CpCcTo
                    ErabAddFailNbr_CpCcTo = KPI_random_val( ErabAddFailNbr_CpCcTo_avg, ErabAddFailNbr_CpCcTo_std_dev, i, T)
                    # ErabAddFailNbr_CpCcFail
                    ErabAddFailNbr_CpCcFail = KPI_random_val( ErabAddFailNbr_CpCcFail_avg, ErabAddFailNbr_CpCcFail_std_dev, i, T)
                    # ErabAddFailNbr_UpGtpFail
                    ErabAddFailNbr_UpGtpFail = KPI_random_val( ErabAddFailNbr_UpGtpFail_avg, ErabAddFailNbr_UpGtpFail_std_dev, i, T)
                    # ErabAddFailNbr_UpMacFail
                    ErabAddFailNbr_UpMacFail = KPI_random_val( ErabAddFailNbr_UpMacFail_avg, ErabAddFailNbr_UpMacFail_std_dev, i, T)
                    # ErabAddFailNbr_UpPdcpFail
                    ErabAddFailNbr_UpPdcpFail = KPI_random_val( ErabAddFailNbr_UpPdcpFail_avg, ErabAddFailNbr_UpPdcpFail_std_dev, i, T)
                    # ErabAddFailNbr_UpRlcFail
                    ErabAddFailNbr_UpRlcFail = KPI_random_val( ErabAddFailNbr_UpRlcFail_avg, ErabAddFailNbr_UpRlcFail_std_dev, i, T)
                    # ErabAddFailNbr_RrcSigFail
                    ErabAddFailNbr_RrcSigFail = KPI_random_val( ErabAddFailNbr_RrcSigFail_avg, ErabAddFailNbr_RrcSigFail_std_dev, i, T)
                    # ErabAddFailNbr_RrcSigTo
                    ErabAddFailNbr_RrcSigTo = KPI_random_val( ErabAddFailNbr_RrcSigTo_avg, ErabAddFailNbr_RrcSigTo_std_dev, i, T)
                    # ErabAddFailNbr_CpBhCacFail
                    ErabAddFailNbr_CpBhCacFail = KPI_random_val( ErabAddFailNbr_CpBhCacFail_avg, ErabAddFailNbr_CpBhCacFail_std_dev, i, T)
                    # ErabAddFailNbr_CpCapaCacFail
                    ErabAddFailNbr_CpCapaCacFail = KPI_random_val( ErabAddFailNbr_CpCapaCacFail_avg, ErabAddFailNbr_CpCapaCacFail_std_dev, i, T)
                    # ErabAddFailNbr_CpQosCacFail
                    ErabAddFailNbr_CpQosCacFail = KPI_random_val( ErabAddFailNbr_CpQosCacFail_avg, ErabAddFailNbr_CpQosCacFail_std_dev, i, T)
                    # ErabAddFailNbr_S1apCuFail
                    ErabAddFailNbr_S1apCuFail = KPI_random_val( ErabAddFailNbr_S1apCuFail_avg, ErabAddFailNbr_S1apCuFail_std_dev, i, T)
                    # ErabAddFailNbr_S1apLinkFail
                    ErabAddFailNbr_S1apLinkFail = KPI_random_val( ErabAddFailNbr_S1apLinkFail_avg, ErabAddFailNbr_S1apLinkFail_std_dev, i, T)
                    # ErabAddFailNbr_S1apSigFail
                    ErabAddFailNbr_S1apSigFail = KPI_random_val( ErabAddFailNbr_S1apSigFail_avg, ErabAddFailNbr_S1apSigFail_std_dev, i, T)
                    # ErabAddFailNbr_CpCcInteraction
                    ErabAddFailNbr_CpCcInteraction = KPI_random_val( ErabAddFailNbr_CpCcInteraction_avg, ErabAddFailNbr_CpCcInteraction_std_dev, i, T)
                    # Init Time val
                    INIT_TIME = timestamp_list[i]

                    # Appending user inputs to csv row
                    csv_row.append(NE_ID)
                    csv_row.append(SYSTEM_ID)
                    csv_row.append(NE_NAME)
                    csv_row.append(INIT_TIME)
                    csv_row.append(TIME_OFFSET)
                    csv_row.append(GRAN_PERIOD)
                    csv_row.append(LOCATION)

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


        

    