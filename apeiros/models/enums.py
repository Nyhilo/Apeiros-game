# Note that the values in this model are not saved to repository.
# It is kept here for hierarchy consistency

from enum import Enum


class LocationType(str, Enum):
    Heat = 'Heat'
    Electricity = 'Electricity'
    Plant = 'Plant'
    Air = 'Air'
    Light = 'Light'
    Cold = 'Cold'
    Water = 'Water'
    Metal = 'Metal'
    Land = 'Land'
    Dark = 'Dark'


class NomsterType(str, Enum):
    # We want to strive to have these two enums in parity, while preserving the
    # clarity in code when using them.
    # In the future, consider a naming refactor for "ElementType" to fuse these
    Heat = LocationType.Heat
    Electricity = LocationType.Electricity
    Plant = LocationType.Plant
    Air = LocationType.Air
    Light = LocationType.Light
    Cold = LocationType.Cold
    Water = LocationType.Water
    Metal = LocationType.Metal
    Land = LocationType.Land
    Dark = LocationType.Dark


class NomsterClass(str, Enum):
    Amphibian = 'Amphibian'
    Arthropoid = 'Arthropoid'
    Avian = 'Avian'
    Piscine = 'Piscine'
    Mammalian = 'Mammalian'
    Reptilian = 'Reptilian'
