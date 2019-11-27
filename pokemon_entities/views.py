import folium
from .models import Pokemon, PokemonEntity

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"
DEFAULT_IMAGE_FOLDER = '/media/'


def add_pokemon(folium_map, lat, lon, name, image_url):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def make_map(request, pokemon_entities):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        pokemon = pokemon_entity.pokemon
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.title_ru,
            get_image_url(request, pokemon.image))
    return folium_map


def get_image_url(request, pokemon_image):
    if pokemon_image == '':
        img_url = DEFAULT_IMAGE_URL
    else:
        img_url = request.build_absolute_uri('/media/') + str(pokemon_image)
    return img_url


def make_all_pokemons_profile(request, pokemons):
    all_pokemons_profile = []
    for pokemon in pokemons:
        all_pokemons_profile.append({
            'pokemon_id': pokemon.id,
            'img_url': get_image_url(request, pokemon.image),
            'title_ru': pokemon.title_ru
        })
    return all_pokemons_profile


def update_pokemon_profile(request, pokemon, pokemon_profile, key):
    pokemon_profile.update(
        {
            key:
                {
                    "title_ru": pokemon.title_ru,
                    "pokemon_id": pokemon.id,
                    "img_url": get_image_url(request, pokemon.image)
                }
        }
    )


def make_pokemon_profile(request, pokemon):

    pokemon_profile = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title_ru,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "img_url": get_image_url(request, pokemon.image)
    }

    try:
        update_pokemon_profile(request, pokemon.previous_evolution, pokemon_profile, 'previous_evolution')
    except AttributeError:
        pass

    try:
        next_evolution_pokemon = pokemon.next_evolution.get()
        update_pokemon_profile(request, next_evolution_pokemon, pokemon_profile, 'next_evolution')
    except ObjectDoesNotExist:
        pass

    return pokemon_profile


def show_all_pokemons(request):

    pokemon_entities = PokemonEntity.objects.all()
    folium_map = make_map(request, pokemon_entities)

    pokemons = Pokemon.objects.all()
    all_pokemons_profile = make_all_pokemons_profile(request, pokemons)
    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': all_pokemons_profile,
    })


def show_pokemon(request, pokemon_id):

    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_profile = make_pokemon_profile(request, pokemon)

    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)

    folium_map = make_map(request, pokemon_entities)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_profile})
