"""SimpleTags file."""
# Django
from django import template

register = template.Library()


@register.filter('get_pk')
def get_pk(value):
    """Get pk from url function.

    Args:
        value (string): url

    Returns:
        int: primary key from url
    """
    value = value.split('/')
    value = value[::-1]
    return int(value[1])


@register.filter('redirect_slashes')
def redirect_slashes(value):
    """Redirect slashes function.

    Args:
        value (string): string with backslashes

    Returns:
        string: string with forward slashes
    """
    value = value.split('\\')
    value = '/'.join(value)
    return f'/{value}'
