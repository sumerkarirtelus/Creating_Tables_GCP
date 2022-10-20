import csv
import math

# Time constants

T = 96

def KPI_random_val(average_val, std_dev_val, t, T):

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



# Writing to csv

with open('tables.csv', 'w', encoding='UTF8', newline='') as f:

    header = ['NE_ID', 'SYSTEM_ID', 'NE_NAME', 'INIT_TIME', 'TIME_OFFSET', 'GRAN_PERIOD', 'LOCATION', 'EstabAddAttNbr', 'EstabAddSuccNbr', 'ErabAddFailNbr_CpCcTo', 'ErabAddFailNbr_CpCcFail', 'ErabAddFailNbr_UpGtpFail', 'ErabAddFailNbr_UpMacFail', 'ErabAddFailNbr_UpPdcpFail', 'ErabAddFailNbr_UpRlcFail', 'ErabAddFailNbr_RrcSigFail', 'ErabAddFailNbr_RrcSigTo', 'ErabAddFailNbr_CpBhCacFail', 'ErabAddFailNbr_CpCapaCacFail', 'ErabAddFailNbr_CpQosCacFail', 'ErabAddFailNbr_S1apCuFail', 'ErabAddFailNbr_S1apLinkFail', 'ErabAddFailNbr_S1apSigFail', 'ErabAddFailNbr_CpCcInteraction']

    writer = csv.writer(f)

    writer.writerow(header)

    for j in range(days):

        for i in range(T):

            #Writing data to the csv file
            csv_row = []
            
            # EstabAddAttNbr
            EstabAddAttNbr = KPI_random_val( 0.14326206673145447, 0.7034359784282516, i, T)
            # EstabAddSuccNbr
            EstabAddSuccNbr = KPI_random_val( 0.14285714285714285, 0.7025391013692989, i, T)
            # ErabAddFailNbr_CpCcTo
            ErabAddFailNbr_CpCcTo = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_CpCcFail
            ErabAddFailNbr_CpCcFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_UpGtpFail
            ErabAddFailNbr_UpGtpFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_UpMacFail
            ErabAddFailNbr_UpMacFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_UpPdcpFail
            ErabAddFailNbr_UpPdcpFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_UpRlcFail
            ErabAddFailNbr_UpRlcFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_RrcSigFail
            ErabAddFailNbr_RrcSigFail = KPI_random_val( 0.00033772374197906115, 0.01837493378931075, i, T)
            # ErabAddFailNbr_RrcSigTo
            ErabAddFailNbr_RrcSigTo = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_CpBhCacFail
            ErabAddFailNbr_CpBhCacFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_CpCapaCacFail
            ErabAddFailNbr_CpCapaCacFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_CpQosCacFail
            ErabAddFailNbr_CpQosCacFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_S1apCuFail
            ErabAddFailNbr_S1apCuFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_S1apLinkFail
            ErabAddFailNbr_S1apLinkFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_S1apSigFail
            ErabAddFailNbr_S1apSigFail = KPI_random_val( 0, 0, i, T)
            # ErabAddFailNbr_CpCcInteraction
            ErabAddFailNbr_CpCcInteraction = KPI_random_val( 0.00008443093549476529, 0.009188630773666186, i, T)

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


        

    