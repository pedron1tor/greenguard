import io
import os
from urllib.parse import urlparse
from pathlib import Path
import environ
from django.core.exceptions import ImproperlyConfigured
# Import the original settings from each template
from .basesettings import *

# Load the settings from the environment variable
env = environ.Env()
env.read_env(io.StringIO(os.environ.get("APPLICATION_SETTINGS", None)))
PROD = True if env('DJANGO_SETTINGS_MODULE') == 'mainframe.settings.prod' else False
# Setting this value from django-environ
SECRET_KEY = env("SECRET_KEY")

if "mainframe" not in INSTALLED_APPS:
  INSTALLED_APPS.append("mainframe")
if "storages" not in INSTALLED_APPS:
  INSTALLED_APPS.append("storages")
# If defined, add service URL to Django security settings
CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
if CLOUDRUN_SERVICE_URL:
  ALLOWED_HOSTS = [
      urlparse(CLOUDRUN_SERVICE_URL).netloc,
      'greenguard.com.mx',
  ]
  CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL, 'https://greenguard.com.mx']
else:
  ALLOWED_HOSTS = ["*"]

DEBUG = env("DEBUG", default=False)

# Set this value from django-environ
DATABASES = {"default": env.db()}

if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
  DATABASES["default"]["HOST"] = "127.0.0.1"
  DATABASES["default"]["PORT"] = 5432
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_DEFAULT_ACL = "publicRead"
DEFAULT_FILE_STORAGE = 'mainframe.cloudstorage.CustomGoogleCloudStorage'