from django.db import models


class modelsform(models.Model):
    ville = models.CharField(max_length=100)
    type_de_vehicule = models.CharField(max_length=100)
    climat = models.CharField(max_length=100)
    condition_economique = models.CharField(max_length=100)
    jour = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)
    vitesse = models.FloatField()
    heure_de_pointe = models.BooleanField(default=False)
    evenement_aleatoire = models.BooleanField(default=False)
    consommation_energetique = models.FloatField()

    def __str__(self):
        return self.ville
    
class doc(models.Model):
    doc = models.FileField()
    linkdin = models.fields.CharField(max_length=200, null=True)
    portfolio = models.fields.CharField(max_length=200, null=True)