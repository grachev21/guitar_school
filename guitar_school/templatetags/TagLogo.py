from django import template


register = template.Library()

@register.inclusion_tag('guitar_school/tag_templates/logo.html')
def logo(**kwargs):
    pass
    # data = {
    #     'count_words': "x"
    # }
    # return data