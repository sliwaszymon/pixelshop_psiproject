"""File that stores filters."""

# 3rd-party
from django_filters import FilterSet
from django_filters import NumberFilter

# Project
from pixelshop.models import PixelArt


class PixelArtFilter(FilterSet):
    """PixelArtFilter class."""

    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        """Meta class."""

        model = PixelArt
        fields = ['title', 'from_price', 'to_price']
