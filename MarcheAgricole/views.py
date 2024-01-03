from django.shortcuts import render
from .models import Produit, Marche, Disponibilite, Demande


def marche_view(request):
    produits = Produit.objects.all()
    marches = Marche.objects.all()
    disponibilites = Disponibilite.objects.all()
    demandes = Demande.objects.all()

    for produit in produits:
        Produit.objects.using('marcheagricole').create(name=produit.name)

    for marche in marches:
        Marche.objects.using('marcheagricole').create(
            produit=marche.produit,
            date=marche.date,
            prix_moyen=marche.prix_moyen,
            tendance=marche.tendance,
            source=marche.source
        )

    for disponibilite in disponibilites:
        Disponibilite.objects.using('marcheagricole').create(
            produit=disponibilite.produit,
            date=disponibilite.date,
            quantite_disponible=disponibilite.quantite_disponible,
            offres_speciales=disponibilite.offres_speciales,
            mois_precedent=disponibilite.mois_precedent,
            mois_actuel=disponibilite.mois_actuel,
            unite_quantite=disponibilite.unite_quantite,
            source=disponibilite.source
        )

    for demande in demandes:
        Demande.objects.using('marcheagricole').create(
            produit=demande.produit,
            date=demande.date,
            niveau_actuel=demande.niveau_actuel,
            prevision=demande.prevision,
            source=demande.source
        )

    return render(request, 'marcheAgricol.html', {
        'produits': produits,
        'marches': marches,
        'disponibilites': disponibilites,
        'demandes': demandes})
