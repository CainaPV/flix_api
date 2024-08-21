from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.PROTECT, related_name= 'reviews' )
    stars = models.IntegerField(validators= [MinValueValidator(0, 'Valor Mínimo aceitável de 0 ESTRELA '), 
                                           MaxValueValidator(5, 'Valor Máximo aceitável de 5 ESTRELAS') ])
    comment = models.TextField(null=True, blank= True)

