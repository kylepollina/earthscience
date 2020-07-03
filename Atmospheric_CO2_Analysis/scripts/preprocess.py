# scripts/preprocess.py

# TODO add license
# TODO add credit to ESRL

import csv
from datetime import date

import data
import pandas

def process_all_data():
    process_mlo_data()
    process_uc_san_diego_data()
    process_global_data()


def process_mlo_data():

    """
    Process CO2 data collected by the Earth Science Research Laboratory
        https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html
    Data collected from the Mauna Loa Observatory in Mauna Loa, Hawaii

    Takes data in co2_weekly_mlo.txt and converts it into a CSV
    """

    with open('data/processed/mlo_co2.csv', 'w+') as mlo_csv_file:
        csvwriter = csv.writer(mlo_csv_file)

        csvwriter.writerow(['Year', 'Month', 'Day', 'Decimal Date', 'Carbon Dioxide (ppm)'])

        # Load unprocessed mlo_data
        with open('data/raw/co2_weekly_mlo.txt', 'r') as file:
            raw_data = file.readlines()[49:]
            
            for row in raw_data:
                data = row.split()
                year = data[0]
                month = data[1]
                day = data[2]
                decimal = data[3] 
                ppm = data[4] if float(data[4]) != -999.99 else ''
                
                csvwriter.writerow([year, month, day, decimal, ppm])


def process_uc_san_diego_data():
    """
    Process CO2 data collected by the Earth Science Research Laboratory
        https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html
    Data collected from the Mauna Loa Observatory in Mauna Loa, Hawaii
    Preprocessed by the University of California San Diego

    Takes data in co2_weekly_mlo.txt and converts it into a CSV
    """

    with open('data/processed/ucsd_co2.csv', 'w+') as ucsd_csv_file:
        csvwriter = csv.writer(ucsd_csv_file)

        # Load unprocessed ucsd data
        ucsd = pandas.read_csv('data/raw/CarbonDioxide.csv')

        # Drop extra data
        ucsd = ucsd.drop(['Seasonally Adjusted CO2 (ppm)', 'Carbon Dioxide Fit (ppm)', 
                    'Seasonally Adjusted CO2 Fit (ppm)'], axis=1)

        ucsd.to_csv(ucsd_csv_file, sep=',', index=False)


def process_global_data():
    """
    Process CO2 data collected by the Earth Science Research Laboratory
        https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html
    Data collected from global sources and averaged out.

    Takes data in co2_trend_gl.txt and converts it into a CSV
    """
    with open('data/processed/co2_global.csv', 'w+') as global_csv_file:
        csvwriter = csv.writer(global_csv_file)

        csvwriter.writerow(['Date', 'Carbon Dioxide (ppm)'])

        # Load unprocessed global co2 data
        with open('data/raw/co2_trend_gl.txt', 'r') as file:
            raw_data = file.readlines()[60:]
            
            for row in raw_data:
                data = row.split()
                year = data[0]
                month = data[1]
                day = data[2]
                ppm = data[4] if float(data[4]) != -999.99 else ''

                date = '-'.join([year, month, day])
                
                csvwriter.writerow([date, ppm])
