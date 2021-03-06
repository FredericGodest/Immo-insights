"""
This is the main module for running Streamlit web application
"""

#Import other modules
from global_function import *
from details import *
from simulator import *
from documentation import *

# App title
st.set_page_config(page_title="Immo Insights")

# Navigation bar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("", ["Global Insights", "Simulateur", "Rapport", "Documentation"])
if selection == "Global Insights":
    Global_insights()
elif selection == "Simulateur":
    Estimator()
elif selection == "Rapport":
    Detail_report()
elif selection == "Documentation":
    Doc()





