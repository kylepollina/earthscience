
import pandas
from . import preprocess

class Load:

    @staticmethod
    def wells_processed():
        return pandas.read_csv('data_fracking/processed/Wells.csv')

    @staticmethod
    def quakes_processed():
        return pandas.read_csv('data_fracking/processed/Quakes.csv')

    @staticmethod
    def wells_raw():
        return pandas.read_csv('data_fracking/raw/InjectionWells.csv')

    @staticmethod
    def quakes_raw():
        return pandas.read_csv('data_fracking/raw/okQuakes.csv')
