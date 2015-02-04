## Installation

In `virtualenv`:

```
$ pip install mezzanine_instagram
```

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
```

In `urls.py`:

```
urlpatterns = patterns(
    '',
    ("^instagram/", include("mezzanine_instagram.urls")),
    ...
)
```

Access your Django admin, settings and enter Instagram client id, secret and username, save. Access Django admin, click `Authorize Instagram`.
