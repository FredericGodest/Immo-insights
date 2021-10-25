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
    :return df_loc: filtered and formatted pandas dataframe for rents
    :return df_global: filtered and formatted pandas dataframe for global indicators on districts
    :return df_vente_total: unfiltered data on sells
    :return df_vente : sells data filtered on the latest years (2020)
    """

    # GET DB Vente
    df_vente_total = pd.read_pickle(r"df_vente_total.pickle")

    # PROD MOD
    if os.environ.get("ENV") == "PROD":
        id = os.environ.get("SHEET_ID")

    # TEST MOD
    else:
        config = dotenv_values(".env")
        id = config["SHEET_ID"]

    # Credentials
    sheet_name = "Rouen_Data"
    url = f"https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    # Import
    df = pd.read_csv(url)
    df = df.drop_duplicates(subset=['Titre Annonce',
                                    'offre [loc/achat]',
                                    'surface [m2]',
                                    'prix au m2 [euros]',
                                   'Localisation',
                                    'Compte'],
                            keep='last')

    # Filtering DATA
    df_loc = df[df["offre [loc/achat]"] == "location"]
    df_loc = df_loc[df_loc["Localisation"].str.startswith("Rouen")]

    # Formating
    columns_index = [3, 4] #index columns to float
    for index in columns_index:
        df_loc.iloc[:, index] = [x.replace(',', '.') for x in df_loc.iloc[:, index]]  # Decimal sep
        df_loc.iloc[:, index] = [x.replace(' €', '') for x in df_loc.iloc[:, index]]  # euros sign
        df_loc.iloc[:, index] = [x.replace('\u202f', '') for x in df_loc.iloc[:, index]]  # thousands sep
        df_loc.iloc[:, index] = df_loc.iloc[:, index].astype(float) # float convertion

    # Filtering on latest years (2020)
    df_vente = df_vente_total[df_vente_total["Années"] == 2020]

    # Group data with mean and count
    df_vente_group = df_vente.groupby(["Quartier"]).mean()
    df_vente_count = df_vente.groupby(["Quartier"]).count()
    df_vente_group["count"] = df_vente_count["valeur_fonciere"]
    df_vente_group = df_vente_group.sort_values("prix au m2", ascending=False)
    df_vente_group = df_vente_group[df_vente_group["count"] > 4]
    df_loc_group = df_loc.groupby(["Localisation"]).mean()
    df_loc_count = df_loc.groupby(["Localisation"]).count()

    # DF Global creation
    df_global = pd.DataFrame()
    df_global["prix au m2 location"] = df_loc_group["prix au m2 [euros]"]
    df_global["nb de location %"] = df_loc_count["prix au m2 [euros]"] / df_loc_count["prix au m2 [euros]"].sum() * 100
    df_global = df_global[df_global["nb de location %"] > 1.5]
    df_global["prix au m2 vente"] = df_vente_group["prix au m2"]
    df_global["nb d'achat %"] = df_vente_count["prix au m2"] / df_vente_count["prix au m2"].sum() * 100
    df_global["latitude"] = df_vente_group["latitude"]
    df_global["longitude"] = df_vente_group["longitude"]
    df_global["rendement brut %"] = df_global["prix au m2 location"] * 12 / df_global["prix au m2 vente"] * 100
    df_global["tension %"] = df_global["nb de location %"] - df_global["nb d'achat %"]
    df_global["indicateur"] = (df_global["tension %"] * 2 + df_global["rendement brut %"]) / 3
    df_global["rank"] = df_global["indicateur"].rank(ascending=True)

    return df_loc, df_global, df_vente_total, df_vente