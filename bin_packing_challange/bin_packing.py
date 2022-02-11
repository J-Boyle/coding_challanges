from typing import NamedTuple
from typing import List
from math import ceil
from timeit import timeit


class Service(NamedTuple):
    discipline: str
    description: str
    width: int  # in mm
    access_maintenance_space: int

    def __repr__(self):
        return self.description


class Bin:
    def __init__(self,
                 capacity: int,
                 name: str = None,
                 items_contained: List[Service] = None
                 ):
        self.capacity = capacity  # width in mm
        self.name = name
        self.items_contained = [] if items_contained == None else items_contained

    def capacity_used(self):
        return sum([service.width + service.access_maintenance_space for service in self.items_contained])

    def capacity_wasted(self):
        return self.capacity - self.capacity_used()


def lower_bound(services: List[Service], bin: Bin) -> float:
    """ The best possible solution in an ideal world"""
    return ceil(sum([(service.width + service.access_maintenance_space) for service in services]) / bin.capacity)


def sort_services_by_size(services: List[Service]) -> List[Service]:
    return sorted(services, key=lambda service: service.width)


def fits_in_bin(service: Service, bin: Bin) -> bool:
    return (bin.capacity_used() + service.width + service.access_maintenance_space) <= bin.capacity


def first_fit_algorithm(services: List[Service], bin_capacity: int) -> List[Bin]:
    bins = [Bin(bin_capacity)]

    for service in services:
        for bin in bins:
            if fits_in_bin(service, bin):
                bin.items_contained.append(service)
                break
        else:
            new_bin = Bin(bin_capacity)
            new_bin.items_contained.append(service)
            bins.append(new_bin)

    return bins


def full_bin_algorithm(services: List[Service], num_corridors: int, corridor_width: float) -> dict:
    pass

def total_bin_utilisation(bins: List[Bin])-> float:
    total_capacity = sum(bin.capacity for bin in bins)
    total_capacity_used = sum(bin.capacity_used() for bin in bins)
    return round((total_capacity_used / total_capacity) * 100, 2)


def print_results(bins: List[Bin]) -> None:
    print(f'Bin QTY: {len(bins)}')
    for bin in bins:
        print('--------')
        print(f'Bin Capacity: {bin.capacity}')
        print(f'Capacity Used: {bin.capacity_used()}')
        print(f'Capacity Wasted: {bin.capacity_wasted()}')
        print(f'Items Contained: {bin.items_contained}')


if __name__ == '__main__':
    tray = Service('elec', 'tray', 300, 200)
    ladder = Service('elec', 'ladder', 900, 200)
    trunking = Service('elec', 'trunking', 150, 200)

    cw_pipe = Service('mech', 'cw_pipe', 65, 200)
    lthw_pipe = Service('mech', 'ltwh_pipe', 40, 200)
    duct = Service('mech', 'duct', 500, 200)

    bcw_pipe = Service('ph', 'bcw_pipe', 67, 200)
    drainage_pipe = Service('ph', 'drainage_pipe', 75, 200)
    spinkler_pipe = Service('ph', 'sprinkler_pipe', 100, 200)

    services = [tray,tray,tray,tray,
                ladder,ladder,ladder,ladder,
                trunking,trunking,
                cw_pipe,cw_pipe,
                lthw_pipe,lthw_pipe,
                duct,duct,duct,duct,
                bcw_pipe,bcw_pipe,bcw_pipe,
                drainage_pipe,drainage_pipe,drainage_pipe,
                spinkler_pipe,spinkler_pipe]

    corridor_width = 2500

    lower_bound_threshold = lower_bound(services, Bin(corridor_width))

    first_fit_bins = first_fit_algorithm(services, corridor_width)

    services_by_decreasing_size = sort_services_by_size(services)[::-1]

    first_fit_decreasing_bins = first_fit_algorithm(services_by_decreasing_size, corridor_width)

    print('*** RESULTS SUMMARY ***')
    print(f'Lower Bound: {lower_bound_threshold}')
    print(f'First Fit Algorithm = QTY: {len(first_fit_bins)}, '
          f'Utilization: {total_bin_utilisation(first_fit_bins)}%')

    print(f'First Fit Decreasing Algorithm = QTY: {len(first_fit_decreasing_bins)},'
          f' Utilization: {total_bin_utilisation(first_fit_bins)}%')

    print('')
    print('*** RESULTS DETAILS ***')

    print('First Fit Algorithm')
    print_results(first_fit_bins)

    print('')
    print('')
    print('First Fit Decreasing Algorithm')
    print_results(first_fit_decreasing_bins)
