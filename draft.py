import pickle
import pandas as pd
from geopy.geocoders import Nominatim
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.optimize import curve_fit
import plotly.express as px
import plotly.figure_factory as ff

quartier = "Rouen - Mont Riboudet"

df_vente_total = pd.read_pickle(r"df_vente_total.pickle")

df_vente = df_vente_total[df_vente_total["Années"] == 2020]

df_precise_vente = df_vente

print(df_precise_vente)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_precise_vente["surface_reelle_bati"],
                         y=df_precise_vente["prix au m2"],
                         mode="markers",
                         name="data réel"))
fig.show()

