from django import template

register = template.Library()

@register.filter(name='multiply100')
def multiply100(value):
    """Multiplies the given numeric value by 100."""
    try:
        return float(value) * 100
    except (ValueError, TypeError):
        return ""
