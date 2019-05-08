from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import Auth, Livre_upload_form
from .models import Livre, Categorie

# Create your views here.


def details(request, categorie = 'droits'):

    class Choice():
        def __init__(self,categorie,items,cover_url):  # Notre méthode constructeur
            self.categorie = categorie
            self.items = items
            self.cover_url = cover_url




    choix =[]
    for e in Categorie.objects.all():
        if e.cover:
            choix.append(Choice(e.value,len(Livre.objects.filter(categorie__value=e.value)),e.cover.url))
        else:
            c = Choice()

    livres = Livre.objects.filter(categorie__value=categorie)



    context = {
        'livres': livres,

        'choix':choix


    }
    return render(request,'books/details.html', context)

def upload(request):

    form = Livre_upload_form(request.POST or None)
    #categories =  Categorie.objects.all()

    context ={
        'form': form
        #'categories': categories
    }
    if request.method=='POST':
        form = Livre_upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('details')
        else:
            form = Livre_upload_form()

    return render(request,'books/fileUpload.html',context)

def login(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = Auth(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        username = form.cleaned_data['username']
        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        valide = True
    else:
        redirect('#')

    context ={
        'form' : form
    }
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'registration/login.html', locals())

def search(request):
    livres = None
    querry = None

    if 'q' in request.GET:
        querry = request.GET.get('q')
        livres = Livre.objects.all().filter(Q(titre__contains=querry)|Q(resume__contains=querry)|Q(auteur__contains=querry)|Q(categorie__value__contains=querry))

    items_found=len(livres)

    class Choice():
        def __init__(self,categorie,items,cover_url):  # Notre méthode constructeur
            self.categorie = categorie
            self.items = items
            self.cover_url = cover_url
    choix =[]
    for e in Categorie.objects.all():
        if e.cover:
            choix.append(Choice(e.value,len(Livre.objects.filter(categorie__value=e.value)),e.cover.url))
        else:
            c = Choice()

    context= {
        'querry': querry,
        'livres': livres,
        'items_found':items_found,
        'choix':choix
    }

    return render(request,'books/search.html', context)
