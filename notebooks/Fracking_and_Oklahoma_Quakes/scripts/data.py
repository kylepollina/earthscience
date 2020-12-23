
import pandas

def wells_processed():
    return pandas.read_csv('data_fracking/processed/Wells.csv')

def quakes_processed():
    return pandas.read_csv('data_fracking/processed/Quakes.csv')

def wells_raw():
    return pandas.read_csv('data_fracking/raw/InjectionWells.csv')

def quakes_raw():
    return pandas.read_csv('data_fracking/raw/okQuakes.csv')
