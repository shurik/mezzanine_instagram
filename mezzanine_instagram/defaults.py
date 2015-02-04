from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting


register_setting(
    name="INSTAGRAM_CLIENT_ID",
    description=_("Register an app at http://instagram.com/developer/"),
    editable=True,
    default="",
)

register_setting(
    name="INSTAGRAM_CLIENT_SECRET",
    editable=True,
    default="",
)

register_setting(
    name="INSTAGRAM_USER_ID",
    editable=True,
    default="",
)
