from django.db import models

CHOICE_NATIOLATY = (('USA', 'Estados Unidos'), ('BR', 'Brasil', ), ('CN', 'China'), ('ING', 'Inglaterra'))

class Actor (models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(blank=True, null = True)
    nationality = models.CharField(max_length=100, choices= CHOICE_NATIOLATY)

    def __str__(self):
        return self.name
