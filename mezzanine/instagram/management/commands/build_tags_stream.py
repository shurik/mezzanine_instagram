from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from django.contrib.sites.models import Site
from instagram import InstagramAPIError
from instagram.client import InstagramAPI
from mezzanine.instagram.models import Tag
from mezzanine.conf import settings


class Command(BaseCommand):
    help = 'Build a media stream based on selected instagram tags'

    def handle(self, *args, **options):
        settings.use_editable()
        site = Site.objects.get_current()
        api = InstagramAPI(client_id=settings.INSTAGRAM_CLIENT_ID,
            client_secret=settings.INSTAGRAM_CLIENT_SECRET)

        # use dict to remove duplicates from list
        data = {}
        tags = Tag.objects.values_list('tag', flat=True)
        for tag in tags:
            for g in api.tag_recent_media(tag_name=tag, as_generator=True, count=20, max_pages=3):
                items, next_page = g
                for item in items:
                    data[item.id] = item

        # sort by date tagged
        data = data.values()
        final_items = sorted(data, key=lambda k: k.created_time, reverse=True)
        cache.set('INSTAGRAM_TAGS_STREAM', final_items, 60*60)
