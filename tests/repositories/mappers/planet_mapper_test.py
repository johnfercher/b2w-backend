from src.domain.entities.planet import Planet
from src.repositories.mappers.planet_mapper import PlanetMapper


def test_domain_to_data_should_work_properly():
    # arrange
    domain = Planet.random()

    # act
    data = PlanetMapper.domain_to_data(domain)

    # assert
    assert data is not None
    assert data["_id"] == domain.id
    assert data["name"] == domain.name
    assert data["terrain"] == domain.terrain
    assert data["climate"] == domain.climate
    assert data["qtd_movies"] == domain.qtd_movies


def test_data_to_domain_should_work_properly():
    # arrange
    random = Planet.random()

    data = PlanetMapper.domain_to_data(random)

    # act
    domain = PlanetMapper.data_to_domain(data)

    # assert
    assert data is not None
    assert random.id == domain.id
    assert random.name == domain.name
    assert random.terrain == domain.terrain
    assert random.climate == domain.climate
    assert random.qtd_movies == domain.qtd_movies
