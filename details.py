"""
This is the module which gives a report for the seller with a given adress,
surface, taxe, rework, etc.
"""

# import libraries
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
    default_taxe = 700
    default_charge = 600
    year = 20
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
    nb_meubles = st.number_input("Pièces à meubler", value=0)
    kt = st.number_input("Facteur de sécurité en %", value=15) / 100
    entretien = st.number_input("Entretien par an (en nombre de loyer)", value=1)
    vacance = st.number_input("Nombre de mois de vacance locative par an", value=1)
    TMI = st.number_input("Taux Marginal d'Imposition en %", value=11) / 100

    # First calculation
    assurance = 0.12 / 100 * loyer * 12  # environ 0.12%
    mensualite = (loyer - (taxe_fonciere / 12 + 0.3 * charge_copro / 12 + assurance / 12 + comptable / 12)) * (1 - kt)
    travaux_lourd = 800 * surface_lourd
    travaux_leger = 300 * surface_leger
    travaux_fenetre = 1300 * windows
    meubles = nb_meubles * 1000
    travaux = travaux_lourd + travaux_leger + travaux_fenetre + meubles
    st.markdown("## Loyers ##")
    st.markdown(
        f"Le loyer estimé est de **{int(loyer)} €** par mois (dont {int(0.7 * charge_copro / 12)} € de charge) pour un {surface} m2 au *{adress}*")

    # Price estimations
    credit = mensualite * (1 - (1 + bank_rate / 12) ** (-12 * year)) / (bank_rate / 12)
    rendement_brut = loyer * 12 / credit * 100
    rendement_net = (loyer * 12 - taxe_fonciere - 0.3 * charge_copro - assurance - comptable) / credit * 100
    cash_flow_brut = loyer - mensualite
    cash_flow_net = loyer - mensualite - (0.3 * charge_copro + taxe_fonciere + assurance + comptable) / 12

    # Rapport
    prix_notaire = credit - travaux
    prix_vente = prix_notaire / 1.08  # -notaire
    st.markdown("## Liste de travaux à prévoir ##")
    st.markdown(f"**{int(travaux_lourd)} €** de travaux lourds.")
    st.markdown(f"**{int(travaux_leger)} €** de travaux leger.")
    st.markdown(f"**{int(travaux_fenetre)} €** de remplacement de fenêtres.")
    st.markdown(f"**{int(meubles)} €** de meubles/décorations.")
    st.markdown(f"Total travaux = {int(travaux)} €")
    st.markdown("## Proposition hors frais de notaire ##")
    st.markdown(f"##### **{int(prix_vente)} €**. Soit **{int(prix_vente / surface)} €/m2**. #####")

    # Data Rendements
    st.markdown("## Rendements ##")
    st.markdown(
        f"Le rendement brut estimé est de **{round(rendement_brut, 2)}%**. Cash flow brut de **{round(cash_flow_brut, 2)}€**")
    st.markdown(
        f"Le rendement net de charge estimé est de **{round(rendement_net, 2)}%**. Cash flow net de **{round(cash_flow_net, 2)}€**")

    # Bilan
    total_in = (loyer) * (12 - vacance)  # Loyer charges comprise (0.7 charge copro comprise)
    entretien = entretien * loyer
    charge_year = taxe_fonciere + (charge_copro * vacance + 0.3 * charge_copro * (12 - vacance)) / 12 + comptable + entretien
    total_out = charge_year + mensualite * 12
    ratio = total_out / total_in * 100
    st.markdown("## Bilan annuel ##")
    st.markdown(f"Total revenus = **{int(total_in)}€**.")
    st.markdown(f"Total dépenses = **{int(total_out)}€**.")
    st.markdown(
        f"Différence = **{int(total_in - total_out)}€**. Ratio sortie/entrée de **{int(ratio)}% (viser 70% mini)**")

    # Impots
    depreciation = prix_vente * 0.9 / 30 + travaux / 5
    charge_year = taxe_fonciere + charge_copro + comptable + entretien + depreciation
    capital_year = credit / year
    interet_year = mensualite * 12 - capital_year
    taxe_micro = loyer * (12 - vacance) * 0.5 * (TMI + 0.172)
    total_in_HC = (loyer - 0.7 * charge_copro / 12) * (12 - vacance)
    taxe_reel = (total_in_HC - charge_year - interet_year) * (TMI + 0.172)

    st.markdown("## Bilan aprés impôts ##")
    st.markdown("### LMNP - Micro BIC ###")
    st.markdown(f"Impôts par an = **{int(taxe_micro)}€**.")
    ratio = (total_out + taxe_micro) / total_in * 100
    st.markdown(
        f"Différence à l'année = **{int(total_in - total_out - taxe_micro)}€**. Ratio sortie/entrée de **{int(ratio)}% **")

    st.markdown("### LMNP - Réel ###")
    st.markdown(f"Impôts par an = **{int(taxe_reel)}€**.")
    ratio = (total_out + taxe_reel) / total_in * 100
    st.markdown(
        f"Différence à l'année = **{int(total_in - total_out - taxe_reel)}€**. Ratio sortie/entrée de **{int(ratio)}% **")