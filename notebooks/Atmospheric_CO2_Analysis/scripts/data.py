# Atmospheric_CO2_Analysis/scripts/data.py

from pathlib import Path
import pandas as pd

from .preprocess import process_mlo_data


def get_mlo_data():
    mlo_path = 'data_acda/processed/mlo_co2.csv'
    if not Path(mlo_path).exists():
        process_mlo_data()

    with open(mlo_path) as mlo:
        return pd.read_csv(mlo)



def uc_san_diego_original():
    return pandas.read_csv('data_acda/raw/CarbonDioxide.csv')


def co2_global():
    try:
        with open('data_acda/processed/co2_global.csv') as co2_global:
            return pd.read_csv(co2_global)
    except FileNotFoundError as e:
        print(e)
        print("Run scripts.preprocess.process_all_data() first.")


def fetch_current_mlo():

    """
    Pull the most recent version of MLO data and 
     save it to XXX
    """

    pass

def fetch_current_global():

    """
    Pull the most recent version of MLO data and 
     save it to XXX
    """

    pass

