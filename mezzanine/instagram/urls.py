from django.conf.urls.defaults import patterns, url

from .views import InstagramView, InstagramOAuthView, InstagramDeleteView

urlpatterns = patterns("mezzanine.instagram.views",
    url("^$", InstagramView.as_view(), name="instagram"),
    url("^oauth/$", InstagramOAuthView.as_view(), name="instagram_oauth"),
    url("^delete/$", InstagramDeleteView.as_view(), name="instagram_delete"),
)
