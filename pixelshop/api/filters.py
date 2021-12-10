from django_filters import FilterSet, NumberFilter


class PriceFilter(FilterSet):
    price_lte = NumberFilter(field_name='price', lookup_expr='lte')
    price_gte = NumberFilter(field_name='price', lookup_expr='gte')
    # sprawdzic czy dziala