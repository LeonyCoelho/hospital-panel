from django import template

register = template.Library()

@register.filter
def cor_status(status):
    cores = {
        'vazia': 'success',
        'cirurgia': 'danger',
        'higienizacao': 'warning',
    }
    return cores.get(status, 'secondary')
