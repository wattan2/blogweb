from django import template

from Users.models import *

register = template.Library()

@register.inclusion_tag('Blog/pagination.html', takes_context=True)
def show_pagination(context, page_obj):
    return {
        'page_obj': page_obj,
    }