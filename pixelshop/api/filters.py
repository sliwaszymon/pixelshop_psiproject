from django_filters import FilterSet, NumberFilter
from pixelshop.models import PixelArt

class PixelArtFilter(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = PixelArt
        fields = ['title', 'from_price', 'to_price']
    