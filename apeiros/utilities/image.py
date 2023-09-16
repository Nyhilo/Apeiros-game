# Contains utilities for converting and checking the properties of images.

from io import BytesIO

from PIL import Image


def check_square(image: bytes) -> (int, int):
    '''
    Checks how square the image is. Returns a tuple indicating how many pixels
     the image is off from being square and the percentage of the difference
     from the short-side of the image. For instance, an image of size 200x210
     would report return (pixels, percent) = (10, 5).

    Args:
        image (bytes): An image byte-input. Should be a png formatted image.
                        Use convert_png if not

    Returns:
        (int, int): (pixels_off, percent_off). Values indicating how far the
                     image is from being square.
    '''
    img = Image.open(BytesIO(image))

    width, height = img.size
    diff = abs(width - height)
    percent = 0 if diff == 0 else int((diff / min(width, height)) * 100)
    return diff, percent


def convert_png(image: bytes) -> bytes:
    '''
    !!Not yet implemented. Will simply return the same image given!!
    Converts an image from an expected format (jpg, etc.) to a png.

    Args:
        image (bytes): An image, probably not a png in format.

    Returns:
        bytes: A png encoded to binary.
    '''
    return bytes
