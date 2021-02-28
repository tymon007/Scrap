from django.contrib import admin

from .models import User, Rekord, KodOdpadu


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'salt')
    fields = ['id', 'username', 'email', 'password', 'salt']


@admin.register(Rekord)
class RekordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'nazwa_metalu', 'content', 'waga', 'kod_odpadu')
    fields = ['id', 'user_id', 'nazwa_metalu', 'content', 'waga', 'kod_odpadu']

@admin.register(KodOdpadu)
class KodOdpaduAdmin(admin.ModelAdmin):
    list_display = ('id', 'opis')
    fields = ['id', 'opis']