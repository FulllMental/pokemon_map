from django.contrib import admin

from .models import Pokemon, PokemonEntity, PokemonElementType

admin.site.register(Pokemon)
admin.site.register(PokemonEntity)
admin.site.register(PokemonElementType)
