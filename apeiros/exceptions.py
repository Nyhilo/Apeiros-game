# Custom exceptions for Apeiros

# Player Exceptions #
class PlayerNotFound(Exception):
    pass


class BadMovementDirection(Exception):
    pass


class BadMovementDistance(Exception):
    pass


# Location Exceptions #

class LocationOverlapError(Exception):
    '''
    Thrown when the program attempts to save a location at a coordinate that
    already contains a location.
    '''
    pass


# Image Exceptions #
class ImageNotSquareError(Exception):
    '''
    Thrown when a given image does not fall within the configured squareness
    requirements.
    '''
    pass
