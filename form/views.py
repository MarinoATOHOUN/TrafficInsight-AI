from ast import Global
from http.client import NON_AUTHORITATIVE_INFORMATION
from django.shortcuts import render, redirect
from form.form import inputform
from form.models import modelsform, doc
from form.normalize_predict import predictions

def results(request):
    predicts = predictions(donnees)
    roules = roule
    return render(request, "form/result.html", {"resultat":predicts,
                                                "roule":roule})

def form(request):
    docs = doc.objects.all()
    global roule
    if request.method == "POST":
        Input = inputform(request.POST)

        if Input.is_valid():
            dataform = Input.cleaned_data
            global donnees
            donnees = []
            for champ in dataform:
                donnees.append(dataform[champ])
            if donnees[1] in ['Autonomous Vehicle', 'car']:
                roule = True
            else:
                roule = False

            modelinstance = modelsform.objects.create(**dataform)
            modelinstance.save()

            return redirect("results")
    else:
        Input = inputform()
    return render(request, "form/index.html", {"inputform":Input,
                                                "doc":docs[0]})