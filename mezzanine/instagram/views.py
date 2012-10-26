from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView, DeleteView
from instagram.client import InstagramAPI
from mezzanine.conf import settings

from .models import Instagram


class InstagramView(TemplateView):
    template_name = "instagram/instagram.html"

    def get_context_data(self, *args, **kwargs):
        try:
            instagram = Instagram.objects.all()[0]
            api = InstagramAPI(access_token=instagram.access_token)
            media, discard = api.user_recent_media(
                user_id=instagram.user_id, count=24)
            return {"media": media}
        except IndexError:
            return {"media": []}


class InstagramOAuthView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        code = self.request.GET.get("code")
        settings.use_editable()
        unauthorized_api = InstagramAPI(client_id=settings.INSTAGRAM_CLIENT_ID,
                                        client_secret=settings.INSTAGRAM_CLIENT_SECRET,
                                        redirect_uri="http://www.oola-sf.com/instagram/oauth/")
        access_token = unauthorized_api.exchange_code_for_access_token(code)
        try:
            instagram = Instagram.objects.all()[0]
            instagram.access_token = access_token[0]
            instagram.user_id = int(access_token[1]['id'])
            instagram.full_name = access_token[1]['full_name']
            instagram.username = access_token[1]['username']
            instagram.save()
        except IndexError:
            Instagram.objects.create(access_token=access_token[0],
                                     user_id=int(access_token[1]['id']),
                                     full_name=access_token[1]['full_name'],
                                     username=access_token[1]['username'])
        return "/admin/"


class InstagramDeleteView(DeleteView):
    success_url = "/admin/"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        super(InstagramDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self):
        try:
            return Instagram.objects.all()[0]
        except IndexError:
            return None
