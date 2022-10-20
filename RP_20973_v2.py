
# Version 2
# Reading data from external csv for the average and standard deviations

import csv
import math
import pandas as pd

# Time constants

T = 96

# inputs (avg_val, std_dev, t(48 or 96), T(total number of days))
def KPI_random_val(average_val, std_dev_val, t, T):

    # handling any null inputs
    if(average_val == None):
        average_val = 0.0
    if(std_dev_val == None):
        std_dev_val = 0.0
    
    # Formula
    y = average_val - average_val * math.sin( 2 * math.pi * t / T)
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

# Hardcoding NEID values
NE_ID = "LTSQC0210037"
SYSTEM_ID = 21009

df = pd.read_csv('Montreal_Island_stats.csv')

# Writing to csv

with open('tables_v2.csv', 'w', encoding='UTF8', newline='') as f:

    with open('Montreal_Island_stats.csv', mode='r') as reference_file:

        df = pd.read_csv('Montreal_Island_stats.csv')

        NEID_df = df[df.NEID == NE_ID]
        print(NEID_df.iloc[0]['NEID'])

        # Reading data from csv and assigning it to the variables
        EstabAddAttNbr_avg = NEID_df.iloc[0]['avg(EstabAddAttNbr(count))']
        EstabAddAttNbr_std_dev = NEID_df.iloc[0]['stdev(EstabAddAttNbr(count))']
        EstabAddSuccNbr_avg = NEID_df.iloc[0]['avg(EstabAddSuccNbr(count))']
        EstabAddSuccNbr_std_dev = NEID_df.iloc[0]['stdev(EstabAddSuccNbr(count))']
        ErabAddFailNbr_CpCcTo_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_CpCcTo(count))']
        ErabAddFailNbr_CpCcTo_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_CpCcTo(count))']
        ErabAddFailNbr_CpCcFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_CpCcFail(count)']
        ErabAddFailNbr_CpCcFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_CpCcFail(count)']
        ErabAddFailNbr_UpGtpFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_UpGtpFail(count))']
        ErabAddFailNbr_UpGtpFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_UpGtpFail(count))']
        ErabAddFailNbr_UpMacFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_UpMacFail(count))']
        ErabAddFailNbr_UpMacFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_UpMacFail(count))']
        ErabAddFailNbr_UpPdcpFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_UpPdcpFail(count))']
        ErabAddFailNbr_UpPdcpFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_UpPdcpFail(count))']
        ErabAddFailNbr_UpRlcFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_UpRlcFail(count))']
        ErabAddFailNbr_UpRlcFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_UpRlcFail(count))']
        ErabAddFailNbr_RrcSigFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_RrcSigFail(count))']
        ErabAddFailNbr_RrcSigFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_RrcSigFail(count))']
        ErabAddFailNbr_RrcSigTo_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_RrcSigTo(count))']
        ErabAddFailNbr_RrcSigTo_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_RrcSigTo(count))']
        ErabAddFailNbr_CpBhCacFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_CpBhCacFail(count))']
        ErabAddFailNbr_CpBhCacFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_CpBhCacFail(count))']
        ErabAddFailNbr_CpCapaCacFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_CpCapaCacFail(count))']
        ErabAddFailNbr_CpCapaCacFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_CpCapaCacFail(count))']
        ErabAddFailNbr_CpQosCacFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_CpQosCacFail(count))']
        ErabAddFailNbr_CpQosCacFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_CpQosCacFail(count))']
        ErabAddFailNbr_S1apCuFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_S1apCuFail(count))']
        ErabAddFailNbr_S1apCuFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_S1apCuFail(count))']
        ErabAddFailNbr_S1apLinkFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_S1apLinkFail(count))']
        ErabAddFailNbr_S1apLinkFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_S1apLinkFail(count))']
        ErabAddFailNbr_S1apSigFail_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_S1apSigFail(count))']
        ErabAddFailNbr_S1apSigFail_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_S1apSigFail(count))']
        ErabAddFailNbr_CpCcInteraction_avg = NEID_df.iloc[0]['avg(ErabAddFailNbr_CpCcInteraction(count))']
        ErabAddFailNbr_CpCcInteraction_std_dev = NEID_df.iloc[0]['stdev(ErabAddFailNbr_CpCcInteraction(count))']


        print(EstabAddSuccNbr_avg)
        print(EstabAddSuccNbr_std_dev)



        header = ['NE_ID', 'SYSTEM_ID', 'NE_NAME', 'INIT_TIME', 'TIME_OFFSET', 'GRAN_PERIOD', 'LOCATION', 'EstabAddAttNbr', 'EstabAddSuccNbr', 'ErabAddFailNbr_CpCcTo', 'ErabAddFailNbr_CpCcFail', 'ErabAddFailNbr_UpGtpFail', 'ErabAddFailNbr_UpMacFail', 'ErabAddFailNbr_UpPdcpFail', 'ErabAddFailNbr_UpRlcFail', 'ErabAddFailNbr_RrcSigFail', 'ErabAddFailNbr_RrcSigTo', 'ErabAddFailNbr_CpBhCacFail', 'ErabAddFailNbr_CpCapaCacFail', 'ErabAddFailNbr_CpQosCacFail', 'ErabAddFailNbr_S1apCuFail', 'ErabAddFailNbr_S1apLinkFail', 'ErabAddFailNbr_S1apSigFail', 'ErabAddFailNbr_CpCcInteraction']

        writer = csv.writer(f)

        writer.writerow(header)

        for j in range(days):

            for i in range(T):

                #Writing data to the csv file
                csv_row = []
                
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
                writer.writerow(csv_row)


        

    