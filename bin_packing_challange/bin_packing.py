from typing import NamedTuple
from typing import List
from timeit import timeit


class Service(NamedTuple):
    MEP: str
    description: str
    width: int  # in mm
    access_maintenance_space: int

    def __repr__(self):
        return self.description


class Bin(NamedTuple):
    capacity: int # width in mm
    name: str = None
    items_contained: List[Service] = []  # ??

    def capacity_used(self):
        return sum([service.width + service.access_maintenance_space for service in self.items_contained])

    def __repr__(self):
        return str(self.capacity_used()) + str(self.items_contained)


def lower_bound(services: List[Service], bin: Bin) -> float:
    """ The best possible solution in an ideal world"""
    return sum([service.width + service.access_maintenance_space for service in services]) / bin.capacity


def sort_services_by_size(services: List[Service]) -> List[Service]:
    # return [service.width for service in services]
    return sorted(services, key=lambda service: service.width)


def fits_in_bin(service: Service, bin: Bin) -> bool:
    return (bin.capacity_used() + service.width + service.access_maintenance_space) <= bin.capacity


def first_fit_algorithm(services: List[Service], bin_capacity: int) -> List[bin]:
    services = sort_services_by_size(services)

    bins = [Bin(bin_capacity)]


    for service in services:
        for bin in bins:
            if fits_in_bin(service, bin):
                bin.items_contained.append(service)
                services.remove(service)
                break
            else:
                new_bin = Bin(bin_capacity)
                new_bin.items_contained.append(service)
                services.remove(service)
                bins.append(new_bin)
                break
    return bins


def first_fit_decreasing_algorithm(services: List[Service], bins: List[Bin]) -> dict:
    services = sort_services_by_size(services).reverse()
    pass


def full_bin_algorithm(services: List[Service], num_corridors: int, corridor_width: float) -> dict:
    pass


if __name__ == '__main__':
    pass
