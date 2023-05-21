from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def notebook(request):
    return render(request, "notebook.html")

def graph(request):
    return render(request, "graph.html")

def team(request):
    return render(request, "team.html")

def graph_overview(request):
    return render(request, "graph_overview.html")

def graph_type(request):
    return render(request, "graph_type.html")

def graph_mutation(request):
    return render(request, "graph_mutation.html")

def graph_evolution(request):
    return render(request, "graph_evolution.html")

def graph_externe(request):
    return render(request, "graph_externe.html")


# graphiques overview


def evolution_nb_ventes(request): #evolution ventes
    return render(request, "overview/evolutionVentes.html")

def prix_moyen_du_m2_par_département(request):
    return render(request, "overview/Prix_moyen_du_m²_par_département.html")

def prix_moyen_du_m2_par_region(request):
    return render(request, "overview/Moyenne du Prix au m² par région.html")

def surface_bati_moyenne_par_departement(request):
    return render(request, "overview/Surface moyenne de la surface bati par departement.html")

def somme_surface_terrains_departement(request):
    return render(request, "overview/Somme de la surface des terrains par département.html")

def top10_transactions_par_ville(request):
    return render(request, "overview/top_10_transactions_par_ville_all.html")

def top6_voies_all(request):
    return render(request, "overview/top6_voies_all.html")

def top6_voies_maisons(request):
    return render(request, "overview/top6_voies_maisons.html")

def valeur_fonciere_par_departement_IDF(request):
    return render(request, "overview/Valeur fonciere par departement IDF.html")

def carte_valeur_fonciere_departement(request):
    return render(request, "overview/Valeur fonciere par departement.html")


#graphiques en fonction du type de local 
def prix_m2_departement_avec_selection_du_type(request):
    return render(request, "type/Prix_m2_avec_selection_type.html")

def prix_m2_type_local_regions(request):
    return render(request, "type/prix_m2_type_local_regions.html")

def qtite_type_local(request):
    return render(request, "type/qtite_type_local.html")

def transaction_type_local(request):
    return render(request, "type/transaction_type_local.html")

def nb_transaction_local_IDF(request):
    return render(request, "type/nb_transaction_local_IDF.html")

def prix_m2_commune_departement_Yvelines(request):
    return render(request, "type/prix_m2_commune_departement_Yvelines.html")

def prix_m2_type_departement_IDF(request):
    return render(request, "type/prix_m2_type_departement_IDF.html")

def proportion_de_maisons_par_département(request):
    return render(request, "type/Proportion de maisons par département.html")

def surface_bati_type_local_region(request):
    return render(request, "type/surface_bati_type_local_region.html")

def valeur_fonciere_type_local_region(request):
    return render(request, "type/valeur_fonciere_type_local_region.html")



#graphiques mutations

def nb_transactions_departement(request):
    return render(request, "mutation/Nombre de transaction par département.html")

def Somme_des_valeurs_foncieres_par_Grand_Est(request):
    return render(request, "mutation/Somme des valeurs foncieres par departement_Grand_Est.html")

def nb_transactions_departement(request):
    return render(request, "mutation/Nombre de transaction par département.html")

def top_departement_nbMutations(request):
    return render(request, "mutation/top_departement_nbMutations.html")

def valeur_fonciere_par_lot(request):
    return render(request, "mutation/valeur_fonciere_par_lot.html")


#graphiques evolution

def prix_m2_region_mois(request):
    return render(request, "evolution/prix_m2_region_mois.html")

def transactions_mois(request):
    return render(request, "evolution/transactions_mois.html")

def Prixm2Annee5ans(request):
    return render(request, "evolution/Prixm2Annee5ans.html")

def Prixm2moyen5ans(request):
    return render(request, "evolution/Prixm2moyen5ans.html")

def Prixm2region5ans(request):
    return render(request, "evolution/Prixm2region5ans.html")

def Prixm2RegionEtAnnee5ans(request):
    return render(request, "evolution/Prixm2RegionEtAnnee5ans.html")

def TransactionRegion5ans(request):
    return render(request, "evolution/TransactionRegion5ans.html")

#graphique externe

def Nombres_Habitants_externe(request):
    return render(request, "externe/Nombres_Habitants_externe.html")

def Pourcentage_Transaction_externe(request):
    return render(request, "externe/Pourcentage_Transaction_externe.html")

