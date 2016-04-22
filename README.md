## Installation

In `virtualenv`:

```
$ pip install mezzanine_instagram
```

## Configuration

In `settings.py`:

```
INSTALLED_APPS = (
    ...
    'mezzanine_instagram',
)

DASHBOARD_TAGS = (
    ...
    ("mezzanine_tags.recent_actions", 'instagram_tags.instagram',),
)

INSTAGRAM_CLIENT_ID = os.getenv('INSTAGRAM_CLIENT_ID')
INSTAGRAM_CLIENT_SECRET = os.getenv('INSTAGRAM_CLIENT_SECRET')
```

Add in `urls.py` before Mezzanine's own catch-all pattern:

```
urlpatterns = patterns(
    '',
    url("^instagram/", include("mezzanine_instagram.urls")),
    ...
)
```

Configure `INSTAGRAM_CLIENT_ID` and `INSTAGRAM_CLIENT_SECRET` environment variables. Access Django admin, click `Authorize Instagram`.

Once you've authorized your site you'll be able to access `/instagram/` in your browser to view the feed for the authorized user.

## Media Stream

Requires a caching mechanism like `Memcached`, `Database` or `Filesystem`. Will not work with `Local-memory` or `Dummy`.

Add a tag or more to use when generating the stream by going to `Dashboard > Tags`. Then run the provided management command to generate the stream.

```
$ python manage.py build_tags_stream
```

Now you can access the `Media` in `Dashboard`. At first all images have a green outline indicating that they'll be shown to the public. Click on the image to exclude it from your stream (the outline will turn red).

We recommend using `cron` or similar to run the management command on a regular basis. Please be aware that Instagram limits how often you can access their API.

The curated media stream is available to the public at `/instagram/tags/`.
