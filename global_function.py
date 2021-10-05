"""
This is the module which gives global insights for data analytics.
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


def objective(x: float, a: float, b: float, c: float) -> float:
    """
    This function is returning the value y of F(x) with the founded parameters a, b and c.
    The parameters are found thanks to scipy module named curve_fit.
    In this case F(x) = b + a * np.exp(-x * c)

    :param x: x of F(x)
    :param a: param a of the curve_fit param results
    :param b: param b of the curve_fit param results
    :param c: param c of the curve_fit param results
    :return Y: the result of F(x)
    """
    return b + a * np.exp(-x * c)

def Global_insights():
    """
    This function gives insights with the given datasets.

    :return: plots to streamlit
    """
    # Titles
    st.title("**Insights immobilier sur Rouen**")
    st.write("Ici vous trouverez des données globales de Rouen en terme de location et de vente immobilière. "
             "Les données de vente viennent de https://www.data.gouv.fr/fr/. "
             "Les données de location viennent de https://leboncoin.fr.")

    # Get Datasets
    df_global = pd.read_pickle(r"df_global.pickle")
    df_loc = pd.read_pickle(r"df_loc.pickle")
    df_vente = pd.read_pickle(r"df_vente.pickle")
    df_vente_total = pd.read_pickle(r"df_vente_total.pickle")
    limite = 100

    # Calculation
    df_loc = df_loc[df_loc["surface [m2]"] < limite]
    surface = df_loc["surface [m2]"].to_numpy()
    price = df_loc["prix au m2 [euros]"].to_numpy()
    popt_loc, _ = curve_fit(objective, surface, price)
    a, b, c = popt_loc

    # Creation of line data
    x_line = np.linspace(min(df_loc["surface [m2]"]), max(df_loc["surface [m2]"]), 100)
    y_line = objective(x_line, a, b, c)

    # Rent Plottings
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=surface, y=price,
                             mode="markers",
                             name="data réel"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line,
                             mode="lines",
                             name="tendance"))
    fig.update_layout(title_text="Loyer au m2 en fonction de la surface",
                      yaxis_title="loyer [euros/m2]",
                      xaxis_title="surface [m2]")
    st.plotly_chart(fig)

    # SELL VS LOCATION
    vente = df_vente[df_vente["surface_reelle_bati"] < limite]["surface_reelle_bati"]
    location = df_loc[df_loc["surface [m2]"] < limite]["surface [m2]"]
    hist_data = [vente, location]
    group_labels = ["Ventes", "Locations"]
    fig = ff.create_distplot(hist_data, group_labels, bin_size=5)
    fig.update_layout(title_text="Nombre de location et de vente en fonction de la surface")
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
    fig.update_layout(title_text="Evolution du prix de vente du m2 en fonction des années",
                      xaxis_title="Années",
                      yaxis_title="Prix de vente [euros/m2]")
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
    fig.update_layout(title_text="Evolution du nombre de vente en fonction des années",
                      xaxis_title="Années",
                      yaxis_title="Nombre de vente")
    st.plotly_chart(fig)

    # MAP Rendement
    fig = px.scatter_mapbox(df_global, lat="latitude", lon="longitude", color="rendement brut %", size="nb de location %",
                            labels="Localisation", color_continuous_scale=px.colors.sequential.thermal, size_max=30,
                            zoom=12,
                            mapbox_style="carto-positron",
                            hover_name=df_global.index)
    fig.update_layout(title_text="Carte des rendements dans les quartiers de Rouen")
    st.plotly_chart(fig)

    # Map nb de vente
    df_vente_total_count = df_vente_total.groupby(["Quartier"]).count()
    df_vente_total_mean = df_vente_total.groupby(["Quartier"]).mean()
    df_map = df_vente_total_mean[["latitude", "longitude"]]
    df_map["nombre de vente"] = df_vente_total_count["latitude"]

    fig = px.scatter_mapbox(df_map, lat="latitude", lon="longitude", color="nombre de vente", size="nombre de vente",
                            labels="Localisation", color_continuous_scale=px.colors.sequential.solar, size_max=30,
                            zoom=12,
                            mapbox_style="carto-positron",
                            hover_name=df_map.index)
    fig.update_layout(title_text="Carte des ventes enregistrées entre 2016 et 2020 les quartiers de Rouen")
    st.plotly_chart(fig)





