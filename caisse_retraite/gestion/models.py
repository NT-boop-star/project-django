from django.db import models

# Create your models here.
from django.db import models

class Adherent(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    numero_securite_sociale = models.CharField(
        max_length=15, 
        unique=True, 
        help_text="Numéro de sécurité sociale unique"
    )
    date_adhesion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Adhérent"
        ordering = ['nom', 'prenom']

class Cotisation(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_versement = models.DateField()
    adherent = models.ForeignKey(
        Adherent, 
        on_delete=models.CASCADE, 
        related_name='cotisations'
    )

    def __str__(self):
        return f"Cotisation de {self.montant}€ pour {self.adherent} le {self.date_versement}"

    class Meta:
        ordering = ['-date_versement']