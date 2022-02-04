

from .base import *
from .base_layout_settings import *
from .base_geo_settings import *
from .local_settings import *

# Determine if we are running a test and import the tests.py at the the end of
# this init
import sys
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'


if DEBUG:
    THIRD_PARTY_APPS.append('debug_toolbar')

G3WADMIN_PROJECT_APPS = G3WADMIN_PROJECT_APPS + G3WADMIN_PROJECT_APPS_BASE
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + G3WADMIN_APPS + G3WADMIN_PROJECT_APPS
MIDDLEWARE = MIDDLEWARE + G3WADMIN_MIDDLEWARE

if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

if SITE_PREFIX_URL:
    VECTOR_URL = '/' + SITE_PREFIX_URL + VECTOR_URL[1:]

try:
    INSTALLED_APPS += G3WADMIN_LOCAL_MORE_APPS
except NameError:
    pass

try:
    if FRONTEND:
        LOGIN_REDIRECT_URL = '/admin/'
except:
    pass

if SENTRY:
    try:
        INSTALLED_APPS += ['raven.contrib.django.raven_compat']

        import os
        import raven

        RAVEN_CONFIG = {
            'dsn': '',
            # If you are using git, you can also automatically configure the
            # release based on the git info.
            'release': raven.fetch_git_sha(os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))),
        }
    except Exception:
        pass


if TESTING:
    try:
        from .tests_settings import *
    except ImportError:
        pass
