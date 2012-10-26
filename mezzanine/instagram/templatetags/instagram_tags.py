from django.template import Library
from mezzanine.instagram.models import Instagram
from mezzanine.instagram.views import unauthorized_api

register = Library()


@register.inclusion_tag("instagram/instagram_authorize.html",
                        takes_context=True)
def instagram(context):
    """
    Renders the Instagram authorize tag
    """
    try:
        context['instagram'] = Instagram.objects.all()[0]
    except IndexError:
        context['instagram'] = None
    context['authorize_url'] = unauthorized_api.get_authorize_url(
        scope=["basic", "likes", "comments", "relationships"])
    return context
