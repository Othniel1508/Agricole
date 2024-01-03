from django.db import models


class Produit(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'produit'


class Marche(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date = models.DateField()
    prix_moyen = models.DecimalField(max_digits=5, decimal_places=2)
    tendance = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    class Meta:
        db_table = 'marche'


class Disponibilite(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date = models.DateField()
    quantite_disponible = models.IntegerField()
    offres_speciales = models.CharField(max_length=200)
    mois_precedent = models.IntegerField()
    mois_actuel = models.IntegerField()
    unite_quantite = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    class Meta:
        db_table = 'disponibilite'


class Demande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date = models.DateField()
    niveau_actuel = models.CharField(max_length=200)
    prevision = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    class Meta:
        db_table = 'demande'
