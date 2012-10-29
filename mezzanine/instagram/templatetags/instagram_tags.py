from django.contrib.sites.models import Site
from django.template import Library
from instagram.client import InstagramAPI
from mezzanine.conf import settings
from mezzanine.instagram.models import Instagram

register = Library()


@register.inclusion_tag("instagram/instagram_authorize.html",
                        takes_context=True)
def instagram(context):
    """Renders the Instagram authorize tag"""
    try:
        context['instagram'] = Instagram.objects.all()[0]
    except IndexError:
        context['instagram'] = None
    settings.use_editable()
    site = Site.objects.get_current()
    conf = {
        "redirect_uri": "http://{0}/instagram/oauth/".format(site.domain),
        "client_id": settings.INSTAGRAM_CLIENT_ID,
        "client_secret": settings.INSTAGRAM_CLIENT_SECRET,
    }
    unauthorized_api = InstagramAPI(**conf)
    context['authorize_url'] = unauthorized_api.get_authorize_url(
        scope=["basic", "likes", "comments", "relationships"])
    return context
