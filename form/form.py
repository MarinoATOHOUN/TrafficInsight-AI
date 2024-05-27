from django import forms

villes = (
    ('Ecoopolis', 'Ecoopolis'),
    ('AquaCity', 'AquaCity'),
    ('Neuroburg', 'Neuroburg'),
    ('SolarisVille', 'SolarisVille'),
    ('MetropolisX', 'MetropolisX'),
    ('TechHaven', 'TechHaven')
)

type_vehicules = (
    ('Autonomous Vehicle', 'Véhicule Autonomes'),
    ('Drone', 'Drone'),
    ('Flying Car', 'Voiture volante'),
    ('Car', 'Voiture')
)

climat =(
    ('Solar Flare', 'Éruption solaire'),
    ('Snowy', 'Neige'),
    ('Electromagnetic Storm', 'Tempête électromagnétique'),
    ('Clear', 'Clair'),
    ('Rainy', 'Pluvieux')
)

condition_economiques = (
    ('Booming', 'En plein essor'),
    ('Recession', 'Récession'),
    ('Stable', 'Stable')
)

jours = (
    ('Monday', 'Lundi'),
    ('Tuesday', 'Mardi'),
    ('Wednesday', 'Mercredi'),
    ('Thursday', 'Jeudi'),
    ('Friday', 'Vendredi'),
    ('Saturday', 'Samedi'),
    ('Sunday', 'Dimanche')
)

heurs = (
    (1, '1 heur AM'),
    (2, '2 heur AM'),
    (3, '3 heur AM'),
    (4, '4 heur AM'),
    (5, '5 heur AM'),
    (6, '6 heur AM'),
    (7, '7 heur AM'),
    (8, '8 heur AM'),
    (9, '9 heur AM'),
    (10, '10 heur AM'),
    (11, '11 heur AM'),
    (12, '12 heur AM'),
    (13, '1 heur PM'),
    (14, '2 heur PM'),
    (15, '3 heur PM'),
    (16, '4 heur PM'),
    (17, '5 heur PM'),
    (18, '6 heur PM'),
    (19, '7 heur PM'),
    (20, '8 heur PM'),
    (21, '9 heur PM'),
    (22, '10 heur PM'),
    (23, '11 heur PM'),
    (24, '12 heur PM')
)

class inputform(forms.Form):
    ville = forms.ChoiceField(
        choices=villes, required=True, 
        label="Ville", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    type_de_vehicule = forms.ChoiceField(
        choices=type_vehicules, 
        required=True, 
        label="Type de véhicule", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    climat = forms.ChoiceField(
        choices=climat, 
        required=True, 
        label="Conditions climatique",
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    condition_economique = forms.ChoiceField(
        choices=condition_economiques, 
        required=True, 
        label="Conditions économique", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    jour = forms.ChoiceField(
        choices=jours, 
        required=True, 
        label="Jour", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    heure = forms.ChoiceField(
        choices=heurs, 
        required=True, 
        label="Heure", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    vitesse = forms.FloatField(
        required=True, 
        label="Vitesse de déplacement", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    heure_de_pointe = forms.BooleanField(
        required=False, 
        label="Heure de pointe ?", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    evenement_aleatoire = forms.BooleanField(
        required=False, 
        label="Evenement aléatoire (accident de circulation, ...)", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )
    consommation_energetique = forms.FloatField(
        required=True, 
        label="Consormation en énergie", 
        error_messages={
            'required': "Veillez entrer un choix valid"
            }
    )