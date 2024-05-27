import pickle
import numpy as np


def tableur(position, len):
    tab = []
    for no in range(len):
        if no == position:
            tab.append(1)
        else:
            tab.append(0)
    return tab

def trad(lst):
    city = ['AquaCity', 'Ecoopolis', 'MetropolisX', 'Neuroburg', 'SolarisVille', 'TechHaven']
    type_vehicule = ['Autonomous Vehicle', 'Car', 'Drone', 'Flying Car']
    climat = ['Clear', 'Electromagnetic Storm', 'Rainy', 'Snowy', 'Solar Flare']
    condition_economique = ['Booming', 'Recession', 'Stable']
    jours = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    
    city = tableur(city.index(lst[0]), len(city))
    type_vehicule = tableur(type_vehicule.index(lst[1]), len(type_vehicule))
    climat = tableur(climat.index(lst[2]), len(climat))
    condition_economique = tableur(condition_economique.index(lst[3]), len(condition_economique))
    jours = tableur(jours.index(lst[4]), len(jours))
    i = [int(i) for i in lst[7:9]]
    result_tab = city + type_vehicule + climat + condition_economique + jours + lst[7:9] + i + lst[9:]
    return np.array(result_tab).reshape(1, -1)

def predictions(lst):
    with open('form/trafic_routier.pkl', 'rb') as fichier_modele:
        modele = pickle.load(fichier_modele)
    donnees_a_predire = trad(lst)
    prediction = modele.predict(donnees_a_predire)
    prediction = float(str(prediction[0])[:6])
    return int(prediction*10000)