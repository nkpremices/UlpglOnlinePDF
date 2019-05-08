from django.shortcuts import render
from books.models import Livre, Categorie
# Create your views here.
def home(request):

    class Choice():
        def __init__(self,categorie,items,cover_url):  # Notre méthode constructeur
            self.categorie = categorie
            self.items = items
            self.cover_url = cover_url




    choix =[]
    for e in Categorie.objects.all():
        if e.cover:
            #you got to raise the cover not given exception, learn about falsy values in python
            choix.append(Choice(e.value,len(Livre.objects.filter(categorie__value=e.value)),e.cover.url))
        else:
            c = Choice


    #nombre_categories = len(categories)

    livres = Livre.objects.all()



    context = {

        'choix':choix
    }
    return render(request, 'base.html', context)