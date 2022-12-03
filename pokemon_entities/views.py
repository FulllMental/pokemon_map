import folium
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(pokemon, folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    popup = f"<b>Название</b>: {pokemon.pokemon.title}<br> \
            <b>Дата появления</b>: {pokemon.appeared_at.strftime('%d/%m/%Y %H:%M')}<br>\
            <b>Дата исчезновения</b>: {pokemon.disappeared_at.strftime('%d/%m/%Y %H:%M')}"
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        popup=popup,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lte=timezone.localtime(), disappeared_at__gte=timezone.localtime())
    for pokemon in pokemon_entities:
        add_pokemon(pokemon,
            folium_map, pokemon.lat,
            pokemon.lon,
            request.build_absolute_uri(pokemon.pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        try:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': request.build_absolute_uri(pokemon.image.url),
                'title_ru': pokemon.title,
            })
        except ValueError:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'title_ru': pokemon.title,
            })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    previous_pokemon = pokemon.previous_evolution
    next_pokemon = pokemon.next_evolutions.first()
    try:
        previous_pokemon_evolution = {
            "pokemon_id": previous_pokemon.id,
            "title_ru": previous_pokemon.title,
            "img_url": request.build_absolute_uri(previous_pokemon.image.url),
        }
    except AttributeError:
        previous_pokemon_evolution = None

    try:
        next_pokemon_evolution = {
            "pokemon_id": next_pokemon.id,
            "title_ru": next_pokemon.title,
            "img_url": request.build_absolute_uri(next_pokemon.image.url),
        }

    except AttributeError:
        next_pokemon_evolution = None

    chosen_pokemon = {
        "title_ru": pokemon.title,
        "img_url": pokemon.image.url,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "previous_evolution": previous_pokemon_evolution,
        "next_evolution": next_pokemon_evolution
    }

    pokemon_entities = PokemonEntity.objects.filter(pokemon__title=pokemon)
    for pokemon in pokemon_entities:
        add_pokemon(pokemon,
            folium_map, pokemon.lat,
            pokemon.lon,
            request.build_absolute_uri(pokemon.pokemon.image.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': chosen_pokemon
    })
