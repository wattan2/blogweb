from django import template

from Users.models import *


register = template.Library()


@register.inclusion_tag('Users/user_form.html', takes_context=True)
def show_form(context, form):
    return {
        'form': form,
    }