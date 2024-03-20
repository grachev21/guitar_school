from django import template


register = template.Library()

@register.inclusion_tag('guitar_school/tag_templates/line.html')
def line(**kwargs):
    pass


@register.inclusion_tag('guitar_school/tag_templates/logo.html')
def logo(**kwargs):
    pass


@register.inclusion_tag('guitar_school/tag_templates/icons.html')
def icons(**kwargs):
    pass