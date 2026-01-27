from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Dodaje CSS class na form field."""
    attrs = field.field.widget.attrs if hasattr(field, 'field') else field.widget.attrs
    attrs['class'] = css_class
    return field
