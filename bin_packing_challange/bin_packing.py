from typing import NamedTuple
from typing import List


class Service(NamedTuple):
    MEP: str
    description: str
    width: int
    access_maintenance_space: int


class Bin(NamedTuple):
    capacity: float
    items_contained: List[Service] = []  #??

    def capacity_used(self):
        return sum([service.width for service in self.items_contained])


def lower_bound(services: List[Service], bins: List[Bin]) -> float:
    """ The best possible solution in an ideal world"""
    services_space = sum([service.width + service.access_maintenance_space for service in services])
    available_corridor_space = sum([bin.capacity for bin in bins])
    return services_space / available_corridor_space


def sort_services_by_size(services: List[Service]) -> List[int]:
    return [service.width for service in services].sort()


def fits_in_bin(service: Service, bin: Bin) -> bool:
    return bin.capacity_used() + service.width < bin.capacity


def first_fit_algorithm(services: List[Service], bins: List[Bin]) -> List[bin]:
    services = sort_services_by_size(services)
    pass



def first_fit_decreasing_algorithm(services: List[Service], bins: List[Bin]) -> dict:
    services = sort_services_by_size(services).reverse()
    pass


def full_bin_algorithm(services: List[Service], num_corridors: int, corridor_width: float) -> dict:
    pass
