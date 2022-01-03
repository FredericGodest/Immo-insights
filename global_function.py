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
    df_loc, df_global, df_vente_total, df_vente, forecast_count, forecast_price = get_data()
    limite = 100

    # Calculation
    df_loc = df_loc[df_loc["surface [m2]"] < limite]
    surface = df_loc["surface [m2]"].to_numpy()
    price = df_loc["prix au m2 [euros]"].to_numpy()
    rent = df_loc["prix [euros]"].to_numpy()
    popt_loc, _ = curve_fit(objective, surface, price)
    a, b, c = popt_loc

    # Params for Sells
    df_vente = df_vente[df_vente["surface_reelle_bati"] < limite]
    surfaces_vente = df_vente["surface_reelle_bati"].to_numpy()
    price_vente = df_vente["prix au m2"].to_numpy()
    popt_vente, _ = curve_fit(objective, surfaces_vente, price_vente)
    g, h, i = popt_vente

    # Creation of line data
    x_line = np.linspace(min(df_loc["surface [m2]"]), max(df_loc["surface [m2]"]), 100)
    y_line = objective(x_line, a, b, c) * x_line

    # Find 2021 approximation with forecast
    last_record = df_vente_total.sort_index().index[-1]
    df1 = df_vente_total[(df_vente_total.index >= "01-01-2021") & (df_vente_total.index <= last_record)]
    df1 = df1.groupby(pd.Grouper(freq="m")).count()
    x1 = df1.valeur_fonciere.sum()
    df = forecast_count[(forecast_count["ds"] >= last_record) & (forecast_count["ds"] <= "31-12-2021")]
    df = df.set_index("ds")
    df = df.groupby(pd.Grouper(freq="m")).sum()
    result = df.trend.sum() + x1


    # Rent Plottings
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=surface, y=rent,
                             mode="markers",
                             name="data réelle"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line,
                             mode="lines",
                             name="tendance"))
    fig.update_layout(title_text=f"Evolution du loyer en fonction de la surface dans Rouen",
                      xaxis_title="Surface en m2",
                      yaxis_title="Loyer en €")
    st.plotly_chart(fig)

    # Plot Sells
    x_line = np.linspace(min(df_vente["surface_reelle_bati"]),
                         max(df_vente["surface_reelle_bati"]),
                         100)
    y_line = objective(x_line, g, h, i)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=surfaces_vente, y=price_vente,
                             mode="markers",
                             name="data réelle"))
    fig.add_trace(go.Scatter(x=x_line, y=y_line,
                             mode="lines",
                             name="tendance ville"))
    fig.update_layout(title_text=f"Evolution du prix de vente en fonction de la surface dans Rouen en 2021",
                      xaxis_title="Surface en m2",
                      yaxis_title="Prix en €/m2")
    st.plotly_chart(fig)


    # SELL preparing data for plotting
    df_vente_total_group = df_vente_total.groupby(["Années"]).mean()
    df_vente_total_count = df_vente_total.groupby(["Années"]).count()
    df_vente_total_count.iloc[-1] = result
    years = df_vente_total_group.index.tolist()
    sell = df_vente_total_group["prix au m2"].tolist()
    count = df_vente_total_count["prix au m2"].tolist()
    years_estimation = np.array([[2016, 2017, 2018, 2019, 2020, 2021, 2022]])

    # PRICE SELL plotting
    # PRIX VENTE
    y = forecast_price.set_index("ds").groupby(pd.Grouper(freq="Y")).mean()["trend"].iloc[:-1]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_vente_total_group.index, y=df_vente_total_group["prix au m2"],
                         name="data réelle"))
    fig.add_trace(go.Bar(x=[years_estimation[0][-1]], y=[y[-1]],
                         name="prédiction"))
    fig.add_trace(go.Scatter(x=years_estimation[0], y=y,
                             mode="lines",
                             name="tendance"))
    fig.update_layout(title_text="Evolution du prix de vente du m2 en fonction des années",
                      xaxis_title="Années",
                      yaxis_title="Prix de vente [€/m2]")
    st.plotly_chart(fig)

    # NUMBER SELL plotting
    df_vente_ma = pd.DataFrame([[result] * len(list(df_vente_total_count.columns))],
                               columns=list(df_vente_total_count.columns), index=['2022'])
    df_sub = df_vente_total_count.append(df_vente_ma)
    df_sub["MA"] = df_sub["prix au m2"].rolling(window=4).mean()

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_vente_total_count.index, y=df_vente_total_count["prix au m2"],
                         name="data réelle"))
    fig.add_trace(go.Bar(x=[df_sub.index[-1]], y=[df_sub.MA.iloc[-1]],
                         name="prédiction"))
    fig.add_trace(go.Scatter(x=df_sub.index, y=df_sub.MA,
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
    fig.update_layout(title_text="Carte des ventes enregistrées entre 2016 et 2021 les quartiers de Rouen")
    st.plotly_chart(fig)





