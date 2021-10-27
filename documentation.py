import streamlit as st

def Doc():
    st.markdown("# Documentation #")
    st.markdown("Bienvenue dans Immo Insight Rouen !")
    st.markdown("Dans cette documentation je vais vous expliquer le fonctionnement de chaque outils"
                " en allant jusqu'aux démonstrationx mathématiques.")
    st.markdown("Le projet se décompose en 3 outils :")
    st.markdown("1. **Global Insights** qui vous donnera des données globales sur la ville de Rouen et ses quartiers.")
    st.markdown("2. **Simulateur** qui vous donnera des données plus local en fonction du quartier et qui estimera le "
                "loyer en fonction du quartier et de la surface.")
    st.markdown("3. **Rapport** qui vous permettra d'aller dans le détail du calcul de rentabilité afin de consolider "
                "votre projet immo.")

    st.markdown("## Global Insights ##")
    st.markdown("Nous allons détailler toutes les données présentées dans leur ordre de passage.")

    st.markdown("### Evolution du loyer en fonction de la surface ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les points bleus sont des données rééls enregistrées à la main sur un Google sheet. "
                "Ces données sont directement extraitent du site leboncoin.fr et sont réguliérement mises à jour")
    st.markdown("#### Courbe de tendance des loyers ####")
    st.markdown("La courbe rouge est la courbe se rapprochant le mieux de tous les points. "
                "Ainsi, nous obtenons une courbe moyenne qui permet d'estimer facilement un loyer moyen en "
                "fonction de la surface.")
    st.markdown("Pour les plus curieux, cette courbe est le résultat d'une fonction d'optimisation exponentielle "
                "entre "
                "le prix en euros/m2 et la surface en m2. "
                "Cette fonction nous donne donc un prix au m2 en fonction de la surface."
                "Si nous voulons obtenir le loyer, il suffit de multiplier cette fonction "
                "par la surface. Et c'est ainsi que nous obtenons la courbe rouge.")

    st.markdown("Enfin, pour les **trés** curieux, voici la fonction en question :")
    st.latex(r'''
    b + a \times \exp^{-surface \times c}
    ''')
    st.markdown("Où a, b et c sont des constantes qui seront recalculée à chaque fois que la jeu"
                "de données sera modifié.")


