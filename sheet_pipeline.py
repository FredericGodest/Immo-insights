"""
This module is gathering data from a remote google sheet.
"""
import pandas as pd
from dotenv import dotenv_values
import os

def get_data():
    """
    This function is gathering data from a remote google sheet.

    :param : None
    :return df_loc: filtered and formatted pandas dataframe"""

    # PROD MOD
    if os.environ.get("ENV") == "PROD":
        id = os.environ.get("sheet_id")

    # TEST MOD
    else:
        config = dotenv_values(".env")
        id = config["SHEET_ID"]

    #Public Credentials
    sheet_name = "Rouen_Data"
    url = f"https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    #Import
    df = pd.read_csv(url)
    df = df.drop_duplicates(subset=['Titre Annonce',
                                    'offre [loc/achat]',
                                    'surface [m2]',
                                    'prix au m2 [euros]',
                                   'Localisation',
                                    'Compte'],
                            keep='last')

    #Filtering DATA
    df_loc = df[df["offre [loc/achat]"] == "location"]
    df_loc = df_loc[df_loc["Localisation"].str.startswith("Rouen")]

    #Formating
    columns_index = [3, 4] #index columns to float
    for index in columns_index:
        df_loc.iloc[:, index] = [x.replace(',', '.') for x in df_loc.iloc[:, index]]  # Decimal sep
        df_loc.iloc[:, index] = [x.replace(' €', '') for x in df_loc.iloc[:, index]]  # euros sign
        df_loc.iloc[:, index] = [x.replace('\u202f', '') for x in df_loc.iloc[:, index]]  # thousands sep
        df_loc.iloc[:, index] = df_loc.iloc[:, index].astype(float) # float convertion

    return df_loc