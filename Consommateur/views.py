from django.shortcuts import render
from .models import Consommateur, RetourProduit, DemandeSpecifique
from django.http import HttpResponseRedirect


def formulaire_consommateur(request):
    if request.method == 'POST':
        consommateur_id = request.POST['consommateur_id']
        bio = request.POST['bio'] == 'true'
        local = request.POST['local'] == 'true'
        sans_gluten = request.POST['sans_gluten'] == 'true'
        vegetarien = request.POST['vegetarien'] == 'true'
        vegetalien = request.POST['vegetalien'] == 'true'

        consommateur = Consommateur(
            consommateur_id=consommateur_id,
            bio=bio,
            local=local,
            sans_gluten=sans_gluten,
            vegetarien=vegetarien,
            vegetalien=vegetalien,
        )
        consommateur.save()

        # You would repeat this for each product review and specific product request in the form
        produit1 = request.POST['produit1']
        avis1 = request.POST['avis1']
        evaluation1 = request.POST['evaluation1']
        date_evaluation1 = request.POST['date_evaluation1']

        retour_produit = RetourProduit(
            consommateur=consommateur,
            produit=produit1,
            avis=avis1,
            evaluation=evaluation1,
            date_evaluation=date_evaluation1,
        )
        retour_produit.save()

        produit_demande1 = request.POST['produit_demande1']
        motif_demande1 = request.POST['motif_demande1']

        demande_specifique = DemandeSpecifique(
            consommateur=consommateur,
            produit_demande=produit_demande1,
            motif_demande=motif_demande1,
        )
        demande_specifique.save()

        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'Consommateur.html')
