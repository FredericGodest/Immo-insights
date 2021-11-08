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
                "Ainsi, nous obtenons une courbe moyenne qui permet d'estimer facilement un prix de vente moyen en "
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

    ###### SIMULATEUR ######

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
    st.markdown("La charge est égale à 70% des charges de copropriété.")

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
    st.markdown("surface = surface totale du bien en m2.")
    st.markdown("##### Travaux lourd #####")
    st.markdown("Le bien a besoin d'être entiérement retapé. L'estimation des travaux est donc :")
    st.latex(r'''
                        travaux = surface \times 800 euros
                    ''')
    st.markdown("Où : ")
    st.markdown("surface = surface totale du bien en m2 ")

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

    st.markdown("#### Calcul des rendements et des cashflow ####")
    st.markdown("On peut distinguer 2 types de rendements et de cash flow; le brut et le net. "
                "Ici les deux sont calculés avec les formules suivantes:")

    st.latex(r'''
                rendement_{brut} = \frac{loyer \times 12}{crédit}
            ''')
    st.latex(r'''
                cashflow_{brut} = loyer - mensualité
            ''')
    st.latex(r'''
                rendement_{net} = \frac{loyer \times 12 - 0.3 \times charge - taxe - assurance - comptable}{crédit}
            ''')
    st.latex(r'''
                cashflow_{net} = loyer - mensualité - \frac{0.3 \times charge - taxe - assurance - comptable}{12}
            ''')

    st.markdown("Où : ")
    st.markdown("loyer = loyer par mensuel")
    st.markdown("crédit = crédit total")
    st.markdown("charge = charges de copropriété")
    st.markdown("taxe = taxe foncière")
    st.markdown("assurance = assurance loyer impayé")
    st.markdown("comptable = coût du comptable")

    st.markdown("### Evolution du loyer en fonction de la surface dans la quartier à l'étude###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les points bleus sont des données rééls enregistrées à la main sur un Google sheet. "
                "Ces données sont directement extraitent du site https://www.leboncoin.fr/ et sont réguliérement mises à jour."
                " Elle sont ensuite filtrées sur le quartier à l'étude.")
    st.markdown("#### Courbe de tendance des loyers ####")
    st.markdown("La courbe rouge est la courbe se rapprochant le mieux de tous les points. "
                "Ainsi, nous obtenons une courbe moyenne qui permet d'estimer facilement un loyer moyen en "
                "fonction de la surface.")
    st.markdown("Pour les plus curieux, cette courbe est le résultat d'une fonction d'optimisation exponentielle "
                "entre "
                "le loyer en euros/m2 et la surface en m2. "
                "Cette fonction nous donne donc un loyer au m2 en fonction de la surface."
                "Si nous voulons obtenir le loyer, il suffit de multiplier cette fonction "
                "par la surface. Et c'est ainsi que nous obtenons la courbe rouge. "
                "La courbe verte représente la tendance au niveau de la ville de Rouen.")

    st.markdown("Enfin, pour les **trés** curieux, voici la fonction en question :")
    st.latex(r'''
        b + a \times \exp^{-surface \times c}
        ''')
    st.markdown("Où a, b et c sont des constantes qui seront recalculées à chaque fois que le jeu"
                "de données sera modifié.")

    st.markdown("### Evolution du prix de vente en euros/m2 en fonction de la surface dans le quartier à l'étude.  ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les points bleus sont des données rééls extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur le quartier et à l'année 2020.")
    st.markdown("#### Courbe de tendance des prix de vente ####")
    st.markdown("La courbe rouge est la courbe se rapprochant le mieux de tous les points. "
                "Ainsi, nous obtenons une courbe moyenne qui permet d'estimer facilement un prix de vente moyen en "
                "fonction de la surface.")
    st.markdown("Pour les plus curieux, cette courbe est le résultat d'une fonction d'optimisation exponentielle "
                "entre "
                "le prix de vente en euros/m2 et la surface en m2. "
                "Cette fonction nous donne donc un prix au m2 en fonction de la surface."
                "Et c'est ainsi que nous obtenons la courbe rouge. "
                "La courbe verte représente la tendance au niveau de la ville de Rouen.")

    st.markdown("Enfin, pour les **trés** curieux, voici la fonction en question :")
    st.latex(r'''
            b + a \times \exp^{-surface \times c}
            ''')
    st.markdown("Où a, b et c sont des constantes qui seront recalculées à chaque fois que le jeu"
                "de données sera modifié.")

    st.markdown("### Courbe de densité des prix de vente###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les points bleus sont des données rééls extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur le quartier et à l'année 2020.")
    st.markdown("#### Courbes de densité ####")
    st.markdown("La courbe bleue représente la densité des prix de vente enregistrées en 2020 dans le quartier en fonction de la "
                "surface.")
    st.markdown("La courbe est accompagnées d'un histogramme afin de quantifier la densité "
                "par échantillons.")

    st.markdown("### Nombre de vente VS nombre de location dans le quartier à l'étude ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("##### Ventes #####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur le quartier et à l'année 2020.")
    st.markdown("##### Locations #####")
    st.markdown("Les données de locations sont enregistrées à la main sur un Google sheet. "
                "Ces données sont directement extraitent du site https://www.leboncoin.fr/ et sont réguliérement mises à jour")
    st.markdown("#### Courbes de densité ####")
    st.markdown("La courbe orange représente la densité de nombre de location disponible dans le quartier en fonction de la "
                "surface.")
    st.markdown("La courbe bleue représente la densité de nombre de vente effectuées en 2020 dans le quartier en fonction de la "
                "surface.")
    st.markdown("Chacunes des courbes sont accompagnées d'histogrammes afin de quantifier la densité "
                "par échantillons.")

    st.markdown("### Evolution du prix de vente en fonction des années dans le quartier à l'étude ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur le quartier.")
    st.markdown("#### Graphique ####")
    st.markdown("Chaque barre représente la moyenne des prix de vente au m2 en fonction des années dans le quartier.")
    st.markdown("La dernière année en rouge (2021) est estimée à l'aide d'une regression linéaire (courbe verte).")

    st.markdown("### Evolution du nombre de vente en fonction des années dans le quartier à l'étude###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur le quartier..")
    st.markdown("#### Graphique ####")
    st.markdown("Chaque barre représente le nombre de vente enregistrées en fonction des années.")
    st.markdown("La dernière année en rouge (2021) est estimée à l'aide d'une regression linéaire (courbe verte).")

    st.markdown("### Carte d'historique des ventes en 2020 dans le quartier ###")
    st.markdown("#### Jeux de données ####")
    st.markdown("Les données de ventes sont extraites du site https://www.data.gouv.fr/fr/ "
                "Ces données sont filtrées sur le quartier.")
    st.markdown("#### Carte ####")
    st.markdown("Les données sont représentées sous forme de bulles dont la couleur change en fonction "
                "du prix au m2 et la taille de la bulle change en fonction de la surface.")

    ###### RAPPORT ######

    st.markdown("## Rapport ##")
    st.markdown("Cet outil permettra de sortir un rapport détaillé un tenant compte de la fiscalité et "
                "en détaillant tous les frais associés.")

    st.markdown("### Données d'entrées ###")
    st.markdown("1. **L'adresse de l'appartement**")
    st.markdown("2. **La surface du bien en m2**")
    st.markdown("3. **Le taux du prêt en %**")
    st.markdown("4. **La taxe foncière en euros/an**")
    st.markdown("5. **Les charges de copropriété en euros/an**")
    st.markdown("6. **Loyer estimé en euros**. "
                "Vous pouvez prendre un précédement estimé à l'aide de l'outil **simulateur**"
                " ou vous pouvez vous baser sur un avis extérieur.")
    st.markdown("7. **La surface à rafraichir en m2**")
    st.markdown("8. **La surface à retaper entièrement en m2**")
    st.markdown("9. **Le nombre de fenêtre à passer en double vitrage**")
    st.markdown("10. **Le nombre de pièce à meubler**")
    st.markdown("11. **Le facteur de sécurité kt en %**")
    st.markdown("12. **Le nombre de loyer passant pour l'entretien du bien**. "
                "Il faut compter 1 mini et 3 maxi pour les bien en location Airbnb.")
    st.markdown("13. **Le nombre de mois de vacance locative**")
    st.markdown("14. **Le taux marginal d'imposition**")

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
    st.markdown("kt = coefficient du sécurité (à affiner dans les données d'entrée)")

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
    st.markdown("##### Travaux legers #####")
    st.markdown("Si un partie du bien a besoin d'un rafraichissement, l'estimation des travaux leger sera :")
    st.latex(r'''
                travaux_{leger} = surface \times 300 euros
                    ''')
    st.markdown("Où : ")
    st.markdown("surface = surface du bien à rafraichir en m2.")
    st.markdown("##### Travaux lourd #####")
    st.markdown("Si une partie du bien a besoin d'être entiérement retapé, l'estimation des travaux lourd sera :")
    st.latex(r'''
                travaux_{lourd} = surface \times 800 euros
                        ''')
    st.markdown("Où : ")
    st.markdown("surface = surface du bien à entiérement retaper en m2 ")
    st.markdown("##### Fenêtre à isoler #####")
    st.markdown("Si le bien à besoin d'avoir des nouvelles fenêtres, la formule est la suivante:")
    st.latex(r'''
                    travaux_{fenêtre} = nb \times 1300 euros
                            ''')
    st.markdown("Où : ")
    st.markdown("nb = nombre de fenêtre à changer ")
    st.markdown("##### Pièce à aménager #####")
    st.markdown("Si le bien à besoin de nouveaux meubles, la formule est la suivante:")
    st.latex(r'''
                        travaux_{meuble} = nb \times 1000 euros
                                ''')
    st.markdown("Où : ")
    st.markdown("nb = nombre de pièces à remeubler ")

    st.markdown("#### Calcul final  des travaux ####")
    st.latex(r'''
                            travaux_{total} = travaux_{leger} + travaux_{lourd} + travaux_{fenêtre} + travaux_{meuble}
                                    ''')


    st.markdown("#### Calcul du prix de vente ####")
    st.markdown("Nous avons maintenant le necessaire pour estimer le prix de vente du bien. "
                "Le formule sera la suivante : ")
    st.latex(r'''
                                prix = \frac{crédit}{1.08} - travaux_{total}
                            ''')
    st.markdown("Où : ")
    st.markdown("prix = prix de vente du bien.")
    st.markdown("crédit = crédit précédement calculé.")
    st.markdown("travaux total = travaux précédement calculés.")
    st.markdown("La division par 1.08 représente les frais de notaire qui montent à 8%.")

    st.markdown("#### Calcul des rendements et des cashflow ####")
    st.markdown("On peut distinguer 2 types de rendements et de cash flow; le brut et le net. "
                "Ici les deux sont calculés avec les formules suivantes:")

    st.latex(r'''
                    rendement_{brut} = \frac{loyer \times 12}{crédit}
                ''')
    st.latex(r'''
                    cashflow_{brut} = loyer - mensualité
                ''')
    st.latex(r'''
                    rendement_{net} = \frac{loyer \times 12 - 0.3 \times charge - taxe - assurance - comptable}{crédit}
                ''')
    st.latex(r'''
                    cashflow_{net} = loyer - mensualité - \frac{0.3 \times charge - taxe - assurance - comptable}{12}
                ''')

    st.markdown("Où : ")
    st.markdown("loyer = loyer par mensuel")
    st.markdown("crédit = crédit total")
    st.markdown("charge = charges de copropriété")
    st.markdown("taxe = taxe foncière")
    st.markdown("assurance = assurance loyer impayé")
    st.markdown("comptable = coût du comptable")

    st.markdown("### Bilan annuel ###")
    st.markdown("Ici on va faire le bilan des entrées et des sorties d'argent en allant dans le détail "
                "et en étant le plus conservateur possible.   "
                "Voici les formules utilisées : ")

    st.latex(r'''
                Entrées = loyer \times (12 - n)
            ''')
    st.latex(r'''
                entretien = loyer \times m
            ''')
    st.latex(r'''
                charges_{annuelles} = taxe + charge \times (n + 0.3 \times (12 - n)) + comptable + entretien + assurance
            ''')
    st.latex(r'''
                Sorties = charges_{annuelles} + mensualité \times 12
            ''')
    st.latex(r'''
                Différence = Entrées - Sorties
            ''')
    st.markdown("Où : ")
    st.markdown("n = nombre de vacance locative")
    st.markdown("m = facteur d'entretien du bien (entre 1 et 3)")
    st.markdown("entretien : coût d'entretien du bien")
    st.markdown("loyer = loyer par mensuel")
    st.markdown("crédit = crédit total")
    st.markdown("charge = charges de copropriété")
    st.markdown("taxe = taxe foncière")
    st.markdown("assurance = assurance loyer impayé")
    st.markdown("comptable = coût du comptable")

    st.markdown("### Bilan annuel aprés impôts ###")
    st.markdown("Pour des raisons de simplicité, ici nous developerons les locations LMNP avec "
                "ses deux régimes les plus connus : Micro BIC et Réél.")

    st.markdown("#### Micro BIC ####")
    st.markdown("On commence par le plus simple avec le formule suivante :")

    st.latex(r'''
                Impôts_{BIC} = \frac{Entrées}{2} \times (TMI + 17,2\%)
            ''')
    st.markdown("Où : ")
    st.markdown("Entrées = les entrées d'argent précédément calculées")
    st.markdown("TMI = Taux Marginal d'Imposition")

    st.markdown("#### Réel ####")
    st.markdown("Ce régime fiscal peut être bien plus avantageux que le précédement mais "
                "en contre partie il est plus complexe à mettre en oeuvre au niveau "
                "comptable.")

    st.markdown("Commençons par calculer la dépreciation du bien en fonction des années. Pour cela "
                "il faut prendre 90% du prix du bien (car 10% réprésentent la surface au sol "
                "qui ne se déprécie pas dans le temps). Il faut ensuite diviser le résultat par 30 car"
                " on considére que, en moyenne, un bien perd complétement sa valeur en 30 ans. "
                "On peut aussi ajouter tous les travaux éventuels qui peuvent être divisé par 5 car, en moyenne "
                "on considère que tous les travaux perdent leur valeur en 5 ans. On obtient donc : ")

    st.latex(r'''
                depreciation = \frac{vente \times 90 \%}{30} + \frac{travaux}{5}
            ''')
    st.markdown("Où : ")
    st.markdown("vente = prix de vente du bien hors frais de notaire")
    st.markdown("travaux = estimation des travaux à effectuer.")

    st.markdown("Dans le régime réel, toutes les charges sont déductibles d'impôts. Nous pouvons donc les sommer :")
    st.latex(r'''
                charges_{annuelles} = taxe + charge \times (n + 0.3 \times (12 - n)) + comptable + entretien + assurance
            ''')
    st.markdown("Cette formule est un copié-collé de la formule précédente.")

    st.markdown("Dans le régime réel on peut aussi déduire les interets que l'on verse "
                "à la banque. Dans un soucis de simplicité et afin d'être conservateur sur le long terme "
                "il est plus sage de lisser les interets sur la durée du prêt afin d'obtenir un coût moyen d'interet "
                "par an. Voici la formule utilisée :")

    st.latex(r'''
                interet_{annuels} = mensualité \times 12 - \frac{crédit}{années}
            ''')
    st.markdown("Où : ")
    st.markdown("mensualité = mensualité du crédit")
    st.markdown("crédit = crédit de la banque")
    st.markdown("années = nombre d'année du crédit (ici 20 par défaut)")

    st.markdown("A l'inverse du régime Micro BIC, ici il faut déduire les charges des entrées.")
    st.latex(r'''
                Entrées_{HT} = (loyer - 70 \% \times charge) \times (12 - n)
            ''')

    st.markdown("Où : ")
    st.markdown("Charge = charges mensualisée")
    st.markdown("n = vacances locatives")

    st.markdown("Vous pouvez maintenant determiner les impôts moyen à payer par an au régime réel:")
    st.latex(r'''
                Impôts_{reel} = (Entrées_{HT} - depreciation - charges_{annuelles} - interet_{annuels}) \times (TMI + 17,2\%)
            ''')

    st.markdown("Les calculs de différence se font avec la formule suivante :")
    st.latex(r'''
                Différence = Entrées - Sorties - Impôts
            ''')

















