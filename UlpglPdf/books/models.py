from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    value = models.CharField(max_length=45)
    cover = models.ImageField(upload_to='books/categories_cover', null=True, blank=True)

    class Meta:
        verbose_name = "categorie"
        ordering = ['value']

    def __str__(self):
        """this method is used for storing courses. matching them to each teacher"""
        return self.value


# Create your models here.

class Livre(models.Model):
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    titre = models.CharField(max_length=45,blank=False,default="...")
    auteur = models.CharField(max_length=45,blank=False,default="...")
    resume = models.TextField(default="...")
    pdf= models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/books_covers/', null=True, blank=True)

    class Meta:
        verbose_name = "livre"
        ordering = ['titre']

    def __str__(self):
        """this method is used for storing courses. matching them to each teacher"""
        return "{0} , {1} . Categorie : {2} ".format(self.auteur,self.titre,self.categorie)
