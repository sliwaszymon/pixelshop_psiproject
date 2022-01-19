"""Project util functions file."""
# Standard Library
import hashlib


def generate_certificate_id(title, desc):
    """Certificate id creation function.

    Args:
        title (string): title of pixelart
        desc (string): description of pixelart

    Returns:
        _Hash: new certificate id
    """
    return hashlib.md5(bytes(title + desc, 'utf-8'))
