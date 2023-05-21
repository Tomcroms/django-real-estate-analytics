"""myProjectDonneesFoncieres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    #header
    path("", views.index, name="index"),
    path("notebook/", views.notebook, name="notebook"),
    path("graph/", views.graph, name="graph"),
    path("team/", views.team, name="team"),
    

    #type de graphe
    path("graph/overview/", views.graph_overview, name="graph_overview"),
    path("graph/type/", views.graph_type, name="graph_type"),
    path("graph/mutation/", views.graph_mutation, name="graph_mutation"),
    path("graph/evolution/", views.graph_evolution, name="graph_evolution"),
    path("graph/externe/", views.graph_externe, name="graph_externe"),


    #graph de type overview
    path("graph/overview/1", views.evolution_nb_ventes, name="graph_overview_1"),
    path("graph/overview/2", views.prix_moyen_du_m2_par_département, name="graph_overview_2"),
    path("graph/overview/3", views.prix_moyen_du_m2_par_region, name="graph_overview_3"),
    path("graph/overview/4", views.surface_bati_moyenne_par_departement, name="graph_overview_4"),
    path("graph/overview/5", views.somme_surface_terrains_departement, name="graph_overview_5"),
    path("graph/overview/6", views.top10_transactions_par_ville, name="graph_overview_6"),
    path("graph/overview/7", views.top6_voies_all, name="graph_overview_7"),
    path("graph/overview/8", views.top6_voies_maisons, name="graph_overview_8"),
    path("graph/overview/9", views.valeur_fonciere_par_departement_IDF, name="graph_overview_9"),
    path("graph/overview/10", views.carte_valeur_fonciere_departement, name="graph_overview_10"),


    #graph de type type de local
    path("graph/type/1", views.prix_m2_departement_avec_selection_du_type, name="graph_type_1"),
    path("graph/type/2", views.prix_m2_type_local_regions, name="graph_type_2"),
    path("graph/type/3", views.qtite_type_local, name="graph_type_3"),
    path("graph/type/4", views.transaction_type_local, name="graph_type_4"),
    path("graph/type/5", views.nb_transaction_local_IDF, name="graph_type_5"),
    path("graph/type/6", views.prix_m2_commune_departement_Yvelines, name="graph_type_6"),
    path("graph/type/7", views.prix_m2_type_departement_IDF, name="graph_type_7"),
    path("graph/type/8", views.proportion_de_maisons_par_département, name="graph_type_8"),
    path("graph/type/9", views.surface_bati_type_local_region, name="graph_type_9"),
    path("graph/type/10", views.valeur_fonciere_type_local_region, name="graph_type_10"),
        

    #graph de type mutation
    path("graph/mutation/1", views.nb_transactions_departement, name="graph_mutation_1"),
    path("graph/mutation/2", views.Somme_des_valeurs_foncieres_par_Grand_Est, name="graph_mutation_2"),
    path("graph/mutation/3", views.nb_transactions_departement, name="graph_mutation_3"),
    path("graph/mutation/4", views.top_departement_nbMutations, name="graph_mutation_4"),
    path("graph/mutation/5", views.valeur_fonciere_par_lot, name="graph_mutation_5"),


    #graph de type evolution
    path("graph/evolution/1", views.prix_m2_region_mois, name="graph_evolution_1"),
    path("graph/evolution/2", views.transactions_mois, name="graph_evolution_2"),

    #default
    path("adminn/", admin.site.urls),
]
