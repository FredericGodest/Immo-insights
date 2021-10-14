"""
This is the module which simulates prices with the given datasets.
It also gives insights for data analytics.
"""

#import libraries
import pickle
import pandas as pd
from geopy.geocoders import Nominatim
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.optimize import curve_fit
import plotly.express as px
import plotly.figure_factory as ff

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
    df_global = pd.read_pickle(r"df_global.pickle")
    df_loc = pd.read_pickle(r"df_loc.pickle")
    df_vente = pd.read_pickle(r"df_vente.pickle")
    df_vente_total = pd.read_pickle(r"df_vente_total.pickle")

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
    default_taxe = 1000
    default_charge = 500
    year = 20
    default_assurance = 120
    dafault_comptable = 40 * 12

    # Users Inputs
    adress = st.text_input("Adresse au format : rue, Rouen", value=default_adress)
    surface = st.number_input("Surface en m2", value=default_surface)
    bank_rate = st.number_input("Taux du prêt immo en %", value=default_bank) / 100
    taxe_fonciere = st.number_input("Taxe foncière en €/an", value=default_taxe)
    charge_copro = st.number_input("Charge de copro en €/an", value=default_charge)
    assurance = st.number_input("Assurance loyer en €/an", value=default_assurance)
    comptable = st.number_input("Prix comptable en €/an", value=dafault_comptable)

    # Geocoding and tests
    locator = Nominatim(user_agent="myGeocoder")
    localisation = locator.geocode(adress)
    try:
        output = str(localisation.raw["display_name"])
    except AttributeError:
        st.markdown("### Il semblerait que l'adresse ne soit pas correcte ###")
        return
    if not "Rouen" in output:
        st.markdown("### Il semblerait que l'adresse ne soit pas dans la ville de Rouen (76100 ou 76000) ###")
        return

    # Databases
    df_global["distance"] = np.sqrt(
            (localisation.latitude - df_global["latitude"]) ** 2 + ((localisation.longitude - df_global["longitude"])) ** 2)
    result = df_global.sort_values(by=["distance"], ascending=True).head(1)
    quartier = result.index[0]
    df_precise_loc = df_loc[df_loc["Localisation"] == quartier]
    df_vente_total = df_vente_total[df_vente_total["Quartier"] == quartier]
    df_precise_vente = df_vente[df_vente["Quartier"] == quartier]
    surfaces = df_precise_loc["surface [m2]"].to_numpy()
    price = df_precise_loc["prix au m2 [euros]"].to_numpy()
    popt_loc, _ = curve_fit(objective, surfaces, price)
    d, e, f = popt_loc
    loyer = surface * objective(surface, d, e, f)  # estimation du loyer

    # First calculation
    mensualite = (loyer - (taxe_fonciere / 12 + charge_copro / 12 + assurance / 12 + comptable / 12)) * 0.9
    travaux_lourd = 800 * surface
    travaux_leger = 300 * surface
    st.markdown("# Loyers #")
    st.markdown(f"Le loyer estimé est de **{int(loyer)} €** par mois (dont {int(0.7 * charge_copro / 12)} € de charge) pour un {surface} m2 au *{adress}*")

    # Price estimations
    credit = mensualite * (1 - (1 + bank_rate / 12) ** (-12 * year)) / (bank_rate / 12)
    rendement_brut = loyer * 12 / credit * 100
    rendement_net = (loyer * 12 - taxe_fonciere - charge_copro - assurance - comptable) / credit * 100
    cash_flow_brut = loyer - mensualite
    cash_flow_net = loyer - mensualite - (taxe_fonciere + charge_copro) / 12
    st.markdown("# Rendements et Prêts #")
    st.markdown("## Rendements ##")
    st.markdown(f"Remboursement en **{year} ans**.")
    st.markdown(f"Le rendement brut estimé est de **{round(rendement_brut, 2)}%**. Cash flow brut de **{round(cash_flow_brut, 2)}€**")
    st.markdown(f"Le rendement net de charge estimé est de **{round(rendement_net, 2)}%**. Cash flow net de **{round(cash_flow_net, 2)}€**")

    # Gros Travaux
    st.markdown("## Prêts ##")
    prix_notaire = credit - travaux_lourd
    prix_vente = prix_notaire / 1.08  # -notaire
    st.markdown("### Gros travaux ###")
    st.markdown(f"**{int(prix_vente)} €** avec des gros travaux. Soit **{int(prix_vente / surface)} €/m2**.")
    st.markdown(f"Négociation : {int(prix_vente * 0.65)}, {int(prix_vente * 0.85)}, {int(prix_vente * 0.95)} ")

    # Petits Travaux
    prix_notaire = credit - travaux_leger
    prix_vente = prix_notaire / 1.08  # -notaire
    st.markdown("### Petits travaux ###")
    st.markdown(f"**{int(prix_vente)} €** avec des petits travaux. Soit **{int(prix_vente / surface)} €/m2**.")
    st.markdown(f"Négociation : {int(prix_vente * 0.65)}, {int(prix_vente * 0.85)}, {int(prix_vente * 0.95)} ")

    # Sans Travaux
    prix_notaire = credit
    prix_vente = prix_notaire / 1.08  # -notaire
    st.markdown("### SANS travaux ###")
    st.markdown(f"**{int(prix_vente)} €** sans travaux. Soit **{int(prix_vente / surface)} €/m2**.")
    st.markdown(f"Négociation : {int(prix_vente * 0.65)}, {int(prix_vente * 0.85)}, {int(prix_vente * 0.95)} ")

    st.markdown(f"# Insights du quartier {quartier} #")
    # Plot Location
    x_line = np.linspace(min(df_loc["surface [m2]"]), max(df_loc["surface [m2]"]), 100)
    y_line = objective(x_line, d, e, f)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=surfaces, y=price,
                             mode="markers",
                             name="data réel"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line,
                             mode="lines",
                             name="approximation"))
    fig.update_layout(title_text=f"Evolution du loyer en fonction de la surface dans le quartier {quartier}",
                      xaxis_title="Surface en m2",
                      yaxis_title="Loyer en €")
    st.plotly_chart(fig)

    # plot density surface
    limite = 100
    vente = df_precise_vente[df_precise_vente["surface_reelle_bati"] < limite]["surface_reelle_bati"]
    location = df_precise_loc[df_precise_loc["surface [m2]"] < limite]["surface [m2]"]
    hist_data = [vente, location]
    group_labels = ["Ventes", "Location"]
    fig = ff.create_distplot(hist_data, group_labels, bin_size=5)
    fig.update_layout(title_text=f"Densité des ventes et des locations en 2020 dans le quartier {quartier}",
                      xaxis_title="Surface en m2")
    st.plotly_chart(fig)

    # SELL preparing data for plotting
    df_vente_total_group = df_vente_total.groupby(["Années"]).mean()
    df_vente_total_count = df_vente_total.groupby(["Années"]).count()

    years = df_vente_total_group.index.tolist()
    sell = df_vente_total_group["prix au m2"].tolist()
    count = df_vente_total_count["prix au m2"].tolist()
    model_count = np.polyfit(years, count, 1)
    model_sell = np.polyfit(years, sell, 1)
    years_estimation = np.array([[2016, 2017, 2018, 2019, 2020, 2021]])
    sell_estimation = model_sell[0] * years_estimation + model_sell[1]
    count_estimation = model_count[0] * years_estimation + model_count[1]

    # PRICE SELL plotting
    # PRIX VENTE
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_vente_total_group.index, y=df_vente_total_group["prix au m2"],
                         name="data réel"))
    fig.add_trace(go.Bar(x=[years_estimation[0][-1]], y=[sell_estimation[0][-1]],
                         name="prédiction"))
    fig.add_trace(go.Scatter(x=years_estimation[0], y=sell_estimation[0],
                             mode="lines",
                             name="tendance"))
    fig.update_layout(title_text=f"Evolution du prix de vente du m2 en fonction des années dans le quartier",
                      xaxis_title="Années",
                      yaxis_title="Prix de vente [€/m2]")
    st.plotly_chart(fig)


    # NUMBER SELL plotting
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_vente_total_count.index, y=df_vente_total_count["prix au m2"],
                         name="data réel"))
    fig.add_trace(go.Bar(x=[years_estimation[0][-1]], y=[count_estimation[0][-1]],
                         name="prédiction"))
    fig.add_trace(go.Scatter(x=years_estimation[0], y=count_estimation[0],
                             mode="lines",
                             name="tendance"))
    fig.update_layout(title_text=f"Evolution du nombre de vente en fonction des années dans le quartier",
                      xaxis_title="Années",
                      yaxis_title="Nombre de vente")
    st.plotly_chart(fig)

    # plot density price
    limite = 100
    vente = df_precise_vente[df_precise_vente["surface_reelle_bati"] < limite]["prix au m2"]
    hist_data = [vente]
    group_labels = ["Ventes"]
    fig = ff.create_distplot(hist_data, group_labels, bin_size=250)
    fig.update_layout(title_text=f"Densité des prix en 2020 dans le quartier {quartier}",
                      xaxis_title="Prix en €")
    st.plotly_chart(fig)

    # plot Map
    fig = px.scatter_mapbox(df_precise_vente, lat="latitude", lon="longitude", color="prix au m2",
                            size="surface_reelle_bati",
                            labels="Localisation", color_continuous_scale=px.colors.sequential.thermal, size_max=30,
                            zoom=14,
                            mapbox_style="carto-positron")
    fig.update_layout(title_text=f"Carte des ventes en 2020 dans le quartier {quartier}")
    st.plotly_chart(fig)