from django import template

register = template.Library()

@register.filter("get_pk")
def get_pk(value):
    value = value.split('/')
    value = value[::-1]
    return int(value[1])