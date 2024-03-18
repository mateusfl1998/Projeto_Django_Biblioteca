from django import template

register = template.Library()

@register.filter(name='teste')   
def mostra_duracao(value1, value2):
    return (value1 - value2).days