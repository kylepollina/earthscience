# scripts/data.py

import pandas as pd

def mlo():
    try:
        with open('data/processed/mlo_co2.csv') as mlo:
            return pd.read_csv(mlo)
    except FileNotFoundError as e:
        print(e)
        print("Run scripts.preprocess.process_all_data() first.")


def ucsd():
    try:
        with open('data/processed/ucsd_co2.csv') as ucsd:
            return pd.read_csv(ucsd)
    except FileNotFoundError as e:
        print(e)
        print("Run scripts.preprocess.process_all_data() first.")

def uc_san_diego_original():
    return pandas.read_csv('data/raw/CarbonDioxide.csv')

def co2_global():
    try:
        with open('data/processed/co2_global.csv') as co2_global:
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

