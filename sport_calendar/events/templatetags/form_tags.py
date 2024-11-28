from django import template

register = template.Library()

@register.inclusion_tag('form_field.html')
def render_field(field):
    return {'field': field}

@register.inclusion_tag('form_field_w_plus_btn.html')
def render_field_w_plus_btn(field):
    return {'field': field}