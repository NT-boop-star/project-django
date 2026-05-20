from django.contrib import admin
from .models import Adherent, Cotisation

class AdherentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_naissance', 'date_adhesion')
    search_fields = ('nom', 'prenom', 'numero_securite_sociale')

class CotisationAdmin(admin.ModelAdmin):
    list_display = ('adherent', 'montant', 'date_versement')
    list_filter = ('date_versement',)

admin.site.register(Adherent, AdherentAdmin)
admin.site.register(Cotisation, CotisationAdmin)

# Register your models here.
