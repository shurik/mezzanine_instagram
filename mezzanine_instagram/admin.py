from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from .models import Tag, Media


class MediaAdmin(admin.ModelAdmin):
    model = Media

    def get_urls(self):
        urls = super(MediaAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^add/$', self.redirect_to_instagram_view),
            url(r'^toggle-media/$', self.admin_site.admin_view(self.toggle_media), name='instagram-toggle-media'),
        )
        return my_urls + urls

    def redirect_to_instagram_view(self, request):
        return HttpResponseRedirect(reverse('admin:instagram_media_changelist'))

    def toggle_media(self, request):
        id = request.REQUEST.get('id')
        try:
            item = Media.objects.get(media_id=id)
            item.delete()
            return HttpResponse('allowed')
        except Media.DoesNotExist, e:
            Media.objects.create(media_id=id, allowed=False)
            return HttpResponse('blocked')

    @method_decorator(ensure_csrf_cookie)
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['instagram_tags_stream_items'] = cache.get('INSTAGRAM_TAGS_STREAM')
        blocked = Media.objects.filter(allowed=False).values_list('media_id', flat=True)
        extra_context['instagram_blocked_media'] = blocked
        view = super(MediaAdmin, self).changelist_view(request, extra_context)
        return view


admin.site.register(Tag)
admin.site.register(Media, MediaAdmin)
