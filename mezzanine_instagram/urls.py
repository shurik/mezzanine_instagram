from django.conf.urls import patterns, url

from .views import (
    InstagramView, InstagramTagsView,
    InstagramOAuthView, InstagramDeleteView, InstagramAjaxView
)

urlpatterns = patterns(
    "mezzanine_instagram.views",
    url("^$", InstagramView.as_view(), name="instagram"),
    url("^tags/$", InstagramTagsView.as_view(), name="instagram_tags"),
    url("^oauth/$", InstagramOAuthView.as_view(), name="instagram_oauth"),
    url("^delete/$", InstagramDeleteView.as_view(), name="instagram_delete"),
    url("^ajax/$", InstagramAjaxView.as_view(), name="instagram_ajax"),
)
