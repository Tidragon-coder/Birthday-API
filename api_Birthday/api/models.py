from django.db import models

# Create your models here.

class Anniversaire(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=60)
    genre = models.CharField(
        max_length=10,
        choices=[("Homme", "Homme"), ("Femme", "Femme"), ("Autre", "Autre")],
        default="Autre"
    )
    date_birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.name} ({self.date_birthday})" # Affichage lisible dans l'admin