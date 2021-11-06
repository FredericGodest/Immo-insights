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
                "Ces données sont directement extraitent du site https://www.leboncoin.fr/ et sont réguliérement mises à jour")
    st.markdown("#### Courbe de tendance des loyers ####")
    st.markdown("La courbe rouge est la courbe se rapprochant le mieux de tous les points. "
                "Ainsi, nous obtenons une courbe moyenne qui permet d'estimer facilement un loyer moyen en "
                "fonction de la surface.")
    st.markdown("Pour les plus curieux, cette courbe est le résultat d'une fonction d'optimisation exponentielle "
                "entre "
                "le loyer en euros/m2 et la surface en m2. "
                "Cette fonction nous donne donc un loyer au m2 en fonction de la surface."
                "Si nous voulons obtenir le loyer, il suffit de multiplier cette fonction "
                "par la surface. Et c'est ainsi que nous obtenons la courbe rouge.")

    st.markdown("Enfin, pour les **trés** curieux, voici la fonction en question :")
    st.latex(r'''
    b + a \times \exp^{-surface \times c}
    ''')
    st.markdown("Où a, b et c sont des constantes qui seront recalculées à chaque fois que le jeu"
                "de données sera modifié.")

    st.markdown("### Evolution du prix de vente en euros/m2 en fonction de la surface ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les points bleus sont des données rééls extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur la commune de Rouen et à l'année 2020.")
    st.markdown("#### Courbe de tendance des prix de vente ####")
    st.markdown("La courbe rouge est la courbe se rapprochant le mieux de tous les points. "
                "Ainsi, nous obtenons une courbe moyenne qui permet d'estimer facilement un loyer moyen en "
                "fonction de la surface.")
    st.markdown("Pour les plus curieux, cette courbe est le résultat d'une fonction d'optimisation exponentielle "
                "entre "
                "le prix de vente en euros/m2 et la surface en m2. "
                "Cette fonction nous donne donc un prix au m2 en fonction de la surface."
                "Et c'est ainsi que nous obtenons la courbe rouge.")

    st.markdown("Enfin, pour les **trés** curieux, voici la fonction en question :")
    st.latex(r'''
        b + a \times \exp^{-surface \times c}
        ''')
    st.markdown("Où a, b et c sont des constantes qui seront recalculées à chaque fois que le jeu"
                "de données sera modifié.")

    st.markdown("### Nombre de vente VS nombre de location ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("##### Ventes #####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur la commune de Rouen et à l'année 2020.")
    st.markdown("##### Locations #####")
    st.markdown("Les données de locations sont enregistrées à la main sur un Google sheet. "
                "Ces données sont directement extraitent du site https://www.leboncoin.fr/ et sont réguliérement mises à jour")
    st.markdown("#### Courbes de densité ####")
    st.markdown("La courbe orange représente la densité de nombre de location disponible en fonction de la "
                "surface.")
    st.markdown("La courbe bleue représente la densité de nombre de vente effectuées en 2020 en fonction de la "
                "surface.")
    st.markdown("Chacunes des courbes sont accompagnées d'histogrammes afin de quantifier la densité "
                "par échantillons.")

    st.markdown("### Evolution du prix de vente en fonction des années ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur la commune de Rouen.")
    st.markdown("#### Graphique ####")
    st.markdown("Chaque barre représente la moyenne des prix de vente au m2 en fonction des années.")
    st.markdown("La dernière année en rouge (2021) est estimée à l'aide d'une regression linéaire (courbe verte).")

    st.markdown("### Evolution du nombre de vente en fonction des années ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur la commune de Rouen.")
    st.markdown("#### Graphique ####")
    st.markdown("Chaque barre représente le nombre de vente enregistrées en fonction des années.")
    st.markdown("La dernière année en rouge (2021) est estimée à l'aide d'une regression linéaire (courbe verte).")

    st.markdown("### Carte des rendements ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("##### Ventes #####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur la commune de Rouen et à l'année 2020.")
    st.markdown("##### Locations #####")
    st.markdown("Les données de locations sont enregistrées à la main sur un Google sheet. "
                "Ces données sont directement extraitent du site https://www.leboncoin.fr/ et sont réguliérement mises à jour")
    st.markdown("#### Carte ####")
    st.markdown("La carte affiche les rendements brut par quartier. " 
                "Le rendement brut est determiné par la formule suivante : ")
    st.latex(r'''
            rendement = \frac{loyer \times 12}{vente} 
            ''')
    st.markdown("Où : ")
    st.markdown("loyer = Loyer moyen enregistré dans le quartier. ")
    st.markdown("vente = prix de vente moyen enregistré dans le quartier. ")
    st.markdown("Le gradient de couleur représente le rendement brut.")
    st.markdown("La taille des bulles représente le nombre de location enregistrées.")

    st.markdown("### Carte des ventes ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur la commune de Rouen et à l'année 2020.")
    st.markdown("#### Carte ####")
    st.markdown("Le gradient de couleur et la taille des bulles représentent le nombre "
                "de vente enregistrées dans le quartier en 2020.")

    st.markdown("## Simulateur ##")
    st.markdown("Cet outil se base sur les données de location afin d'estimer un loyer en fonction du quartier.")

    st.markdown("### Données d'entrées ###")
    st.markdown("Les champs d'entrées sont les suivants :")
    st.markdown("1. **L'adresse de l'appartement**. L'adresse permettra au simulateur de retrouver le quartier "
                "et de filter les données.")
    st.markdown("2. **La surface du bien en m2**")
    st.markdown("3. **Le taux du prêt en %**")
    st.markdown("4. **La taxe foncière en euros/an**")
    st.markdown("5. **Les charges de copropriété en euros/an**")

    st.markdown("### Estimation du loyer ###")
    st.markdown("L'estimation du loyer se fait en calculant la fonction qui determine le loyer "
                "en fonction de la surface. Cette fonction sera expliquée un peu plus bas.")

    st.markdown("### Estimation des prix de vente ###")
    st.markdown("Le but de ce calcul est d'obtenir un bien où le loyer couvre l'ensemble des dépenses."
                "La finalité étant évidement d'obtenir un cash flow positif ou nul.")
    st.markdown("#### Calcul de mensualité ####")
    st.markdown("Voici la formule pour determiner la mensualité de crédit max en fonction du loyer estimé.")
    st.latex(r'''
                mensualité = (loyer - taxe - charge - assurance - comptable) \times (1 - kt)
                ''')
    st.markdown("Où : ")
    st.markdown("loyer = loyer par mois")
    st.markdown("taxe = taxe foncière mensualisé")
    st.markdown("charge = charge de copropriété mensualisé")
    st.markdown("assurance = assurance loyer impayé (0.12% du loyer)")
    st.markdown("comptable = coût du comptable au mois (40 euros)")
    st.markdown("kt = coefficient du sécurité (ici 15%)")

    st.markdown("#### Calcul du crédit ####")
    st.markdown("La mensualité de crédit peut nous donner le crédit à l'aide de la formule suivante:")
    st.latex(r'''
                crédit = mensualité \times {\Bigg(1 - \Big(1 + \frac{taux}{12}\Big)}^{ \frac{-12 \times années}{taux / 12}}\Bigg)
            ''')
    st.markdown("Où : ")
    st.markdown("mensualité = mensualité précédement calculée")
    st.markdown("taux = taux du prêt banquaire")
    st.markdown("années = temps de remboursement du prêt (20 ans)")

    st.markdown("#### Estimation des travaux ####")
    st.markdown("##### Pas de travaux #####")
    st.markdown("Le bien est comme neuf donc travaux = 0 euros")
    st.markdown("##### Travaux legers #####")
    st.markdown("Le bien a besoin d'un rafraichissement. L'estimation des travaux est donc :")
    st.latex(r'''
                    travaux = surface \times 300 euros
                ''')
    st.markdown("Où : ")
    st.markdown("surface = surface du bien en m2.")
    st.markdown("##### Travaux lourd #####")
    st.markdown("Le bien a besoin d'être entiérement retapé. L'estimation des travaux est donc :")
    st.latex(r'''
                        travaux = surface \times 800 euros
                    ''')
    st.markdown("Où : ")
    st.markdown("surface = surface du bien en m2 ")

    st.markdown("#### Calcul du prix de vente ####")
    st.markdown("Nous avons maintenant le necessaire pour estimer le prix de vente du bien. "
                "Le formule sera la suivante : ")
    st.latex(r'''
                            prix = \frac{crédit}{1.08} - travaux
                        ''')
    st.markdown("Où : ")
    st.markdown("prix = prix de vente du bien.")
    st.markdown("crédit = crédit précédement calculé.")
    st.markdown("travaux = travaux précédement calculés.")
    st.markdown("La division par 1.08 représente les frais de notaire qui montent à 8%.")













