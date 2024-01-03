from django.db import models


class Consommateur(models.Model):
    consommateur_id = models.CharField(max_length=200, unique=True)

    # Food Preferences
    bio = models.BooleanField(default=False)
    local = models.BooleanField(default=False)
    sans_gluten = models.BooleanField(default=False)
    vegetarien = models.BooleanField(default=False)
    vegetalien = models.BooleanField(default=False)


class Produit(models.Model):
    nom = models.CharField(max_length=200, unique=True)


class RetourProduit(models.Model):
    consommateur = models.ForeignKey(Consommateur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    avis = models.TextField()
    evaluation = models.IntegerField()
    date_evaluation = models.DateField()


class DemandeSpecifique(models.Model):
    consommateur = models.ForeignKey(Consommateur, on_delete=models.CASCADE)
    produit_demande = models.CharField(max_length=200)
    motif_demande = models.TextField()
