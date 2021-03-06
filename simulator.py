"""
This is the module which simulates prices with the given datasets.
It also gives insights for data analytics.
"""

#import libraries
import pickle
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.optimize import curve_fit
import plotly.express as px
import plotly.figure_factory as ff
from sheet_pipeline import *

def objective(x: float, a: float, b: float, c: float) -> float:
    """
    This function is returning the value y of F(x) with the founded parameters a, b and c.
    The parameters are found thanks to scipy module named curve_fit.
    In this case F(x) = b + a * np.exp(-x * c)

    :param x: x of F(x)
    :param a: param a of the curve_fit param results
    :param b: param b of the curve_fit param results
    :param c: param c of the curve_fit param results
    :return Y: the result of F(x)"""
    return b + a * np.exp(-x * c)

def Estimator():
    """
    This function is predicting the price of the appartement with a given adress,
    surface, taxe, etc.
    It will also gives insights throught ploted data.

    :return: results and plots to streamlit
    """
    # Get Datasets
    df_loc, df_global, df_vente_total, df_vente, forecast_count, forecast_price = get_data()
    limite = 100
    dropdown = tuple(df_loc["Localisation"].drop_duplicates())

    # Find 2021 approximation with forecast
    last_record = df_vente_total.sort_index().index[-1]
    df1 = df_vente_total[(df_vente_total.index >= "01-01-2021") & (df_vente_total.index <= last_record)]
    df1 = df1.groupby(pd.Grouper(freq="m")).count()
    x1 = df1.valeur_fonciere.sum()
    df = forecast_count[(forecast_count["ds"] >= last_record) & (forecast_count["ds"] <= "31-12-2021")]
    df = df.set_index("ds")
    df = df.groupby(pd.Grouper(freq="m")).sum()
    result = df.trend.sum() + x1
    ratio_count = result / df_vente_total.groupby(["Années"]).count().iloc[-2]["valeur_fonciere"]

    # Titles
    st.title("Simulateur d'achat et insights de quartier")
    st.write("Bienvenue dans le simulateur de prix d'appartement. Ce simulateur se base sur l'adresse,"
             " la surface, les charges de copropriété, les taxes foncières et le taux du prêt."
             " Ce simulateur vous donnera aussi des données pertinentes sur le quartier sous forme de graphique.")
    st.write("Les données de vente viennent de https://www.data.gouv.fr/fr/. "
             "Les données de location viennent de https://leboncoin.fr.")

    # Default values
    default_adress = "35 place du général de Gaulle, Rouen"
    default_surface = 25
    default_bank = 1.15
    default_taxe = 700
    default_charge = 600
    year = 20

    # Users Inputs 1
    quartier =  st.selectbox('Dans quel quartier le bien est il situé ?', dropdown)
    surface = st.number_input("Surface en m2", value=default_surface)
    taxe_fonciere = st.number_input("Taxe foncière en €/an", value=default_taxe)
    charge_copro = st.number_input("Charge de copro en €/an", value=default_charge)


    df_loc = df_loc[df_loc["surface [m2]"] < limite]
    df_precise_loc = df_loc[df_loc["Localisation"] == quartier]
    df_vente_total = df_vente_total[df_vente_total["Quartier"] == quartier]
    df_precise_vente = df_vente[df_vente["Quartier"] == quartier]
    # Get global data
    surfaces = df_loc["surface [m2]"].to_numpy()
    price = df_loc["prix au m2 [euros]"].to_numpy()
    popt_loc, _ = curve_fit(objective, surfaces, price)
    a, b, c = popt_loc

    # Get precise data
    surfaces = df_precise_loc["surface [m2]"].to_numpy()
    price = df_precise_loc["prix au m2 [euros]"].to_numpy()
    rent = df_precise_loc["prix [euros]"].to_numpy()
    popt_loc, _ = curve_fit(objective, surfaces, price)
    d, e, f = popt_loc

    # Params for Sells global
    surfaces_vente = df_vente["surface_reelle_bati"].to_numpy()
    price_vente = df_vente["prix au m2"].to_numpy()
    popt_vente, _ = curve_fit(objective, surfaces_vente, price_vente)
    j, k, l = popt_vente

    # Params for Sells local
    surfaces_vente = df_precise_vente["surface_reelle_bati"].to_numpy()
    price_vente = df_precise_vente["prix au m2"].to_numpy()
    popt_vente, _ = curve_fit(objective, surfaces_vente, price_vente)
    g, h, i = popt_vente

    # Compute Rent in the neighbhoor
    loyer_first = surface * objective(surface, d, e, f)  # estimation du loyer
    st.markdown("## Loyers estimé basé sur data#")
    st.markdown(
        f"Le loyer estimé est de **{int(loyer_first)} €** par mois (dont {int(0.7 * charge_copro / 12)} € de charge) pour un {surface} m2 à *{quartier}*")

    #input 2
    loyer = st.number_input("Loyer par mois (à corriger avec visite)", value=loyer_first)
    prix_vente_site = st.number_input("Prix de vente (prix idéal par défaut)", value=loyer_first * 12 / 0.06)
    vacance = st.number_input("Vacance locative en mois/an", value=1)
    bank_rate = st.number_input("Taux du prêt immo en %", value=default_bank) / 100

    prix_ideal = int(loyer * 12 / 0.06)
    prix_ideal_format = "{:,}".format(prix_ideal).replace(',', ' ')
    st.markdown("## Prix de vente estimé basé sur rendement 6%#")
    st.markdown(f"Prix de vente mini conseillé = {prix_ideal_format}€")


    # First calculation
    assurance = 0.12 / 100 * loyer * 12  # environ 0.12%
    mensualite = prix_vente_site / ((1 - (1 + bank_rate / 12) ** (-12 * year)) / (bank_rate / 12))
    travaux_lourd = 800 * surface
    travaux_leger = 300 * surface

    # Price estimations
    LOYER = (12 - vacance) * loyer # A l'année
    CHARGE_COPRO = (0.3 * (12-vacance)/12 + vacance/12) * charge_copro # A l'année

    rendement_brut = LOYER / prix_vente_site * 100
    rendement_net = (LOYER - taxe_fonciere - CHARGE_COPRO - assurance - mensualite * 12) / prix_vente_site * 100
    cash_flow_brut = LOYER/12 - mensualite
    cash_flow_net = LOYER/12 - mensualite - (CHARGE_COPRO + taxe_fonciere + assurance) / 12
    cash_flow_allin = LOYER/12 - (CHARGE_COPRO + taxe_fonciere + assurance) / 12
    rendement_allin = (LOYER - taxe_fonciere - CHARGE_COPRO - assurance) / prix_vente_site * 100

    st.markdown("# Rendements et Prêts (avec prix de vente affiché)#")
    st.markdown("## Rendements ##")
    st.markdown(f"Remboursement en **{year} ans**.")
    st.markdown(f"Le rendement brut estimé est de **{round(rendement_brut, 2)}%**. Cash flow brut mensuel de **{round(cash_flow_brut, 2)}€**")
    st.markdown("### Avec Crédit 20 ans ###")
    st.markdown(f"Le rendement net de charge avec crédit est de **{round(rendement_net, 2)}%**. Cash flow net mensuel de **{round(cash_flow_net, 2)}€**")
    st.markdown("### Sans Crédit ###")
    st.markdown(
        f"Le rendement net de charge sans crédit est de **{round(rendement_allin, 2)}%**. Cash flow net mensuel de **{round(cash_flow_allin, 2)}€**")

    # Gros Travaux
    st.markdown("## Prêts ##")
    prix_vente = prix_vente_site - travaux_lourd
    st.markdown("### Gros travaux ###")
    st.markdown(f"**{int(prix_vente)} €** avec des gros travaux. Soit **{int(prix_vente / surface)} €/m2**.")
    st.markdown(f"Négociation : {int(prix_vente * 0.65)}, {int(prix_vente * 0.85)}, {int(prix_vente * 0.95)} ")

    # Petits Travaux
    prix_vente = prix_vente_site - travaux_leger
    st.markdown("### Petits travaux ###")
    st.markdown(f"**{int(prix_vente)} €** avec des petits travaux. Soit **{int(prix_vente / surface)} €/m2**.")
    st.markdown(f"Négociation : {int(prix_vente * 0.65)}, {int(prix_vente * 0.85)}, {int(prix_vente * 0.95)} ")

    # Sans Travaux
    prix_vente = prix_vente_site
    st.markdown("### SANS travaux ###")
    st.markdown(f"**{int(prix_vente)} €** sans travaux. Soit **{int(prix_vente / surface)} €/m2**.")
    st.markdown(f"Négociation : {int(prix_vente * 0.65)}, {int(prix_vente * 0.85)}, {int(prix_vente * 0.95)} ")

    st.markdown(f"# Insights du quartier {quartier} #")

    # Plot Location
    x_line = np.linspace(min(df_loc["surface [m2]"]), max(df_loc["surface [m2]"]), 100)
    y_line = objective(x_line, d, e, f) * x_line
    y_line_global = objective(x_line, a, b, c) * x_line
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=surfaces, y=rent,
                             mode="markers",
                             name="data réelle"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line,
                             mode="lines",
                             name="tendance quartier"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line_global,
                             mode="lines",
                             name="tendance ville"))
    fig.update_layout(title_text=f"Evolution du loyer en fonction de la surface dans le quartier",
                      xaxis_title="Surface en m2",
                      yaxis_title="Loyer en €")
    st.plotly_chart(fig)

    # Plot Sells
    x_line = np.linspace(min(df_precise_vente["surface_reelle_bati"]),
                         max(df_precise_vente["surface_reelle_bati"]),
                         100)
    y_line = objective(x_line, g, h, i)
    y_line_global = objective(x_line, j, k, l)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=surfaces_vente, y=price_vente,
                             mode="markers",
                             name="data réelle"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line,
                             mode="lines",
                             name="tendance quartier"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line_global,
                             mode="lines",
                             name="tendance ville"))
    fig.update_layout(title_text=f"Evolution du prix de vente en fonction de la surface dans le quartier en 2021",
                      xaxis_title="Surface en m2",
                      yaxis_title="Prix en €/m2")
    st.plotly_chart(fig)

    # plot density price
    limite = 100
    vente = df_precise_vente[df_precise_vente["surface_reelle_bati"] < limite]["prix au m2"]
    hist_data = [vente]
    group_labels = ["Ventes"]
    fig = ff.create_distplot(hist_data, group_labels, bin_size=250)
    fig.update_layout(title_text=f"Densité des prix en 2021 dans le quartier",
                      xaxis_title="Prix en €")
    st.plotly_chart(fig)

    # SELL preparing data for plotting
    df_vente_total_group = df_vente_total.groupby(["Années"]).mean()
    df_vente_total_count = df_vente_total.groupby(["Années"]).count()
    df_vente_total_count.iloc[-1] = ratio_count * df_vente_total_count.iloc[-2]["prix au m2"]
    years = df_vente_total_group.index.tolist()
    sell = df_vente_total_group["prix au m2"].tolist()
    count = df_vente_total_count["prix au m2"].tolist()
    model_count = np.polyfit(years, count, 1)
    model_sell = np.polyfit(years, sell, 1)
    years_estimation = np.array([[2016, 2017, 2018, 2019, 2020, 2021, 2022]])
    sell_estimation = model_sell[0] * years_estimation + model_sell[1]
    count_estimation = model_count[0] * years_estimation + model_count[1]

    # PRICE SELL plotting
    # PRIX VENTE
    y = forecast_price.set_index("ds").groupby(pd.Grouper(freq="Y")).mean()["trend"].iloc[:-1]
    ratio = y.iloc[-1] / y.iloc[-2]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_vente_total_group.index, y=df_vente_total_group["prix au m2"],
                         name="data réelle"))
    fig.add_trace(go.Bar(x=[years_estimation[0][-1]], y=[df_vente_total_group["prix au m2"].iloc[-1]*ratio],
                         name="prédiction"))
    fig.add_trace(go.Scatter(x=years_estimation[0], y=y,
                             mode="lines",
                             name="tendance ville"))
    fig.update_layout(title_text=f"Evolution du prix de vente du m2 en fonction des années dans le quartier",
                      xaxis_title="Années",
                      yaxis_title="Prix de vente [€/m2]")
    st.plotly_chart(fig)


    # NUMBER SELL plotting
    result = df_vente_total_count.iloc[-1]["prix au m2"]
    df_vente_ma = pd.DataFrame([[result] * len(list(df_vente_total_count.columns))],
                               columns=list(df_vente_total_count.columns), index=['2022'])
    df_sub = df_vente_total_count.append(df_vente_ma)
    df_sub["MA"] = df_sub["prix au m2"].rolling(window=4).mean()

    fig = go.Figure()
    df_vente_total_count["MA"] = df_vente_total_count["prix au m2"].rolling(window=2).mean()
    fig.add_trace(go.Bar(x=df_vente_total_count.index, y=df_vente_total_count["prix au m2"],
                         name="data réelle"))
    fig.add_trace(go.Bar(x=[df_sub.index[-1]], y=[df_sub.MA.iloc[-1]],
                         name="prédiction"))
    fig.add_trace(go.Scatter(x=df_sub.index, y=df_sub.MA,
                             mode="lines",
                             name="tendance"))
    fig.update_layout(title_text=f"Evolution du nombre de vente en fonction des années dans le quartier",
                      xaxis_title="Années",
                      yaxis_title="Nombre de vente")
    st.plotly_chart(fig)

    # plot Map
    fig = px.scatter_mapbox(df_precise_vente, lat="latitude", lon="longitude", color="prix au m2",
                            size="surface_reelle_bati",
                            labels="Localisation", color_continuous_scale=px.colors.sequential.thermal, size_max=30,
                            zoom=14,
                            mapbox_style="carto-positron")
    fig.update_layout(title_text=f"Carte des ventes en 2021 dans le quartier")
    st.plotly_chart(fig)