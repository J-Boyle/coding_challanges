import pytest

from bin_packing_challange.bin_packing import Service, sort_services_by_size, Bin, fits_in_bin, first_fit_algorithm


@pytest.fixture
def electrical_ladder():
    return Service(MEP='elec',
                   description='ladder',
                   width=450,
                   access_maintenance_space=100)


@pytest.fixture
def electrical_basket():
    return Service(MEP='elec',
                   description='basket',
                   width=300,
                   access_maintenance_space=100)


@pytest.fixture
def mechanical_duct():
    return Service(MEP='mech',
                   description='duct',
                   width=500,
                   access_maintenance_space=100)


@pytest.fixture
def misc_large_services():
    return Service(MEP='misc',
                   description='misc',
                   width=3500,
                   access_maintenance_space=100)


@pytest.fixture
def bin():
    return Bin(2500)


def test_sort_services_by_size(electrical_basket, electrical_ladder, mechanical_duct):
    assert sort_services_by_size([electrical_basket, electrical_ladder, mechanical_duct]) == [electrical_basket,
                                                                                              electrical_ladder,
                                                                                              mechanical_duct]


def test_fits_in_bin(mechanical_duct, bin):
    assert fits_in_bin(mechanical_duct, bin) == True


def test_does_not_fit_in_bin(misc_large_services, bin):
    assert fits_in_bin(misc_large_services, bin) == False


def test_first_fit_algorithm(electrical_basket, electrical_ladder, mechanical_duct):
    print(first_fit_algorithm([electrical_basket, electrical_ladder, mechanical_duct], 900))
