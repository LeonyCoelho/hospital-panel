from django import template

register = template.Library()

@register.filter
def cor_status(status):
    cores = {
        'disponivel': 'success',
        'cirurgia': 'danger',
        'higienizacao': 'warning',
    }
    return cores.get(status, 'secondary')


@register.filter
def get(dictionary, key):
    return dictionary.get(key)


@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name, None)
