"""
This is the module which gives a report for the seller with a given adress,
surface, taxe, rework, etc.
"""

#import libraries
import streamlit as st

def Detail_report():
    """
    This function is printing a report for the seller with a given adress,
    surface, taxe, rework, etc.

    :return: results and plots to streamlit
    """
    # Titles
    st.title("Rapport d'achat et offre de prix")
    st.write("Bienvenue dans l'outil de rapport d'offre d'achat. Ce simulateur se base sur l'adresse,"
             " la surface, les charges de copropriété, les taxes foncières, les travaux et le taux du prêt.")

    # Default values
    default_adress = "35 place du général de Gaulle, Rouen"
    default_surface = 25
    default_bank = 1.15
    default_taxe = 1000
    default_charge = 500
    year = 20
    assurance = 120
    comptable = 40 * 12
    default_loyer = 500

    # Users Inputs
    adress = st.text_input("Adresse au format : rue, Rouen", value=default_adress)
    surface = st.number_input("Surface en m2", value=default_surface)
    bank_rate = st.number_input("Taux du prêt immo en %", value=default_bank) / 100
    taxe_fonciere = st.number_input("Taxe foncière en €/an", value=default_taxe)
    charge_copro = st.number_input("Charge de copro en €/an", value=default_charge)
    loyer = st.number_input("Loyer estimé en €/mois", value=default_loyer)
    surface_leger = st.number_input("Surface à légérement rénover en m2", value=0)
    surface_lourd = st.number_input("Surface à rénover complétement en m2", value=0)
    windows = st.number_input("Nombre de fenêtre à passer en double vitrage", value=0)


    # First calculation
    mensualite = loyer * 0.8 - (taxe_fonciere / 12 + charge_copro / 12)
    travaux_lourd = 800 * surface_lourd
    travaux_leger = 300 * surface_leger
    travaux_fenetre = 1300 * windows
    travaux = travaux_lourd + travaux_leger + travaux_fenetre
    st.markdown("## Loyers ##")
    st.markdown(f"Le loyer estimé est de **{int(loyer)} €** par mois pour un {surface} m2 au *{adress}*")

    # Price estimations
    credit = mensualite * (1 - (1 + bank_rate / 12) ** (-12 * year)) / (bank_rate / 12)
    rendement_brut = loyer * 12 / credit * 100
    rendement_net = (loyer * 12 - taxe_fonciere - charge_copro - assurance - comptable) / credit * 100
    cash_flow_brut = loyer - mensualite
    cash_flow_net = loyer - mensualite - (charge_copro + taxe_fonciere + assurance + comptable) / 12

    # Rapport
    prix_notaire = credit - travaux
    prix_vente = prix_notaire / 1.08  # -notaire
    st.markdown("## Liste de travaux à prévoir ##")
    st.markdown(f"**{int(travaux_lourd)} €** de travaux lourds.")
    st.markdown(f"**{int(travaux_leger)} €** de travaux leger.")
    st.markdown(f"**{int(travaux_fenetre)} €** de remplacement de fenêtres.")
    st.markdown(f"Total travaux = {int(travaux)} €")
    st.markdown("## Proposition hors frais de notaire ##")
    st.markdown(f"##### **{int(prix_vente)} €**. Soit **{int(prix_vente / surface)} €/m2**. #####")

    #data Perso
    st.markdown("# Rendements et Prêts #")
    st.markdown("## Rendements ##")
    st.markdown(f"Remboursement en **{year} ans**.")
    st.markdown(f"Le rendement brut estimé est de **{round(rendement_brut, 2)}%**. Cash flow brut de **{round(cash_flow_brut, 2)}€**")
    st.markdown(f"Le rendement net de charge estimé est de **{round(rendement_net, 2)}%**. Cash flow net de **{round(cash_flow_net, 2)}€**")


