
import pandas as pd
from datetime import datetime

WELLS_PATH_RAW = 'data_fracking/raw/InjectionWells.csv'
QUAKES_PATH_RAW = 'data_fracking/raw/okQuakes.csv'
WELLS_PATH = 'data_fracking/processed/Wells.csv'
QUAKES_PATH = 'data_fracking/processed/Quakes.csv'


def preprocess():
    """Preprocess all data and store in data_fracking/processed"""
    preprocess_wells()
    preprocess_quakes()


def preprocess_wells():
    wells_data = pd.read_csv(WELLS_PATH_RAW)

    wells_data = wells_data.drop(columns=[
        'API#', 'Operator ID', 'WellName', 'QQQQ', 
        'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20',
        'Sec', 'Twp', 'Rng'])

    wells_data = _wells_add_date_time(wells_data)
    wells_data = _wells_add_well_count(wells_data)
    wells_data = _wells_remove_outliers(wells_data)
   
    return wells_data
    

def _wells_add_date_time(wells_data):
    years = []
    months = []
    days = []
    time = []
    well_count = []

    # add date time values
    for index, row in wells_data.iterrows():
        # If you can parse the date
        try:
            date = row['Approval Date']
            month = int(date.split('/')[0])
            day = int(date.split('/')[1])
            year = int(date.split('/')[2])
            years.append(year)
            months.append(month)
            days.append(day)
            time.append(datetime(year, month, day))

        # Else, drop the row
        except: 
            wells_data = wells_data.drop(index)

    wells_data['year'] = years
    wells_data['month'] = months
    wells_data['day'] = days
    wells_data['time'] = time

    return wells_data.sort_values('time').reset_index(drop=True)

def _wells_add_well_count(wells_data):
    _2D_count = 0
    _2d_count = 0
    _2R_count = 0
    _2RSI_count = 0
    CDW_count = 0
    GS_count = 0

    well_count = []

    # add well count 
    for index, row in wells_data.iterrows():
        if row['WellType'] == '2D':
            _2D_count += 1
            well_count.append(_2D_count)
        if row['WellType'] == '2d':
            _2d_count += 1
            well_count.append(_2d_count)
        elif row['WellType'] == '2R':
            _2R_count += 1
            well_count.append(_2R_count)
        elif row['WellType'] == '2RSI':
            _2RSI_count += 1
            well_count.append(_2RSI_count)
        elif row['WellType'] == 'CDW':
            CDW_count += 1
            well_count.append(CDW_count)
        elif row['WellType'] == 'GS':
            GS_count += 1
            well_count.append(GS_count)

    wells_data['well_count'] = well_count
    return wells_data.sort_values('time').reset_index(drop=True)

def _wells_remove_outliers(wells_data):
    """Removes wells located outside the United States"""
    wells_data = wells_data.drop(wells_data.index[5170])
    wells_data = wells_data.drop(wells_data.index[5545])
    wells_data = wells_data.drop(wells_data.index[5775])
    wells_data = wells_data.drop(wells_data.index[6568])
    wells_data = wells_data.drop(wells_data.index[8412])
    wells_data = wells_data.drop(wells_data.index[9119])
    wells_data = wells_data.drop(wells_data.index[10670])
    wells_data = wells_data.drop(wells_data.index[11036])
    wells_data = wells_data.drop(wells_data.index[11057])
    wells_data = wells_data.drop(wells_data[(wells_data['LAT'] == 0) & (wells_data['LONG'] == 0)].index)
    return wells_data.reset_index(drop=True)

def preprocess_quakes():
    quakes_data = pd.read_csv(QUAKES_PATH_RAW)

    years = []
    months = []
    days = []
    time = []

    for index, row in quakes_data.iterrows():
        # If you can parse the date
        try:
            _time = row['time']
            date = _time.split('T')[0]
            year = date.split('-')[0]
            month = date.split('-')[1]
            day = date.split('-')[2]
            years.append(year)
            months.append(month)
            days.append(day)
            time.append(datetime.fromisoformat(_time.split('T')[0]))
        # Else, drop the row
        except:
            quakes_data = quakes_data.drop(index)

    quakes_data['year'] = years
    quakes_data['months'] = months
    quakes_data['days'] = days
    quakes_data['time'] = time

    return quakes_data.sort_values('time').reset_index(drop=True)
