# mlo.py
# Process data from Mauna Loa observatory into a readable CSV format

import csv

class MLO:
    def scrape(self):
        # TODO 
        pass
        
    def write(self):
        # TODO
        pass

print('Processing ML data...')

with open('data/MLO/MaunaLoaWeeklyCO2_2019.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    csvwriter.writerow(['Year', 'Month', 'Day', 'Decimal Date', 'Carbon Dioxide (ppm)'])
    
    with open('data/MLO/co2_weekly_mlo.txt') as file:
        raw_data = file.readlines()[49:]
        
        for row in raw_data:
            data = row.split()
            year = data[0]
            month = data[1]
            day = data[2]
            decimal = data[3] 
            ppm = data[4] if float(data[4]) != -999.99 else ''
            
            csvwriter.writerow([year, month, day, decimal, ppm])

print('Data processed.')
