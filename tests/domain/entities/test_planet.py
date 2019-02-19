from src.domain.entities.planet import Planet


def test_planet_random():
    # act
    planet = Planet.random()

    # assert
    assert planet is not None
    assert planet.id is not None
    assert planet.name is not None
    assert planet.terrain is not None
    assert planet.climate is not None
    assert planet.qtd_movies is not None


def test_planet_init():
    # arrange
    random = Planet.random()

    # act
    planet = Planet(id=random.id, name=random.name, terrain=random.terrain, climate=random.climate, qtd_movies=random.qtd_movies)

    # assert
    assert planet is not None
    assert planet.id == random.id
    assert planet.name == random.name
    assert planet.terrain == random.terrain
    assert planet.climate == random.climate
    assert planet.qtd_movies == random.qtd_movies


def test_planet_from_json():
    # arrange
    random = Planet.random()

    json = {
        "id": random.id,
        "name": random.name,
        "terrain": random.terrain,
        "climate": random.climate,
        "qtd_movies": random.qtd_movies
    }

    # act
    planet = Planet.from_json(json)

    # assert
    assert planet is not None
    assert planet.id == random.id
    assert planet.name == random.name
    assert planet.terrain == random.terrain
    assert planet.climate == random.climate
    assert planet.qtd_movies == random.qtd_movies

