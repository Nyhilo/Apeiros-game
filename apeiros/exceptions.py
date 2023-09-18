# Custom exceptions for Apeiros

class LocationOverlapError(Exception):
    '''
    Thrown when the program attempts to save a location at a coordinate that
    already contains a location.
    '''
    pass
