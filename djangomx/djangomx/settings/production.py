from __future__ import absolute_import
from .common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = SECRETS.get('email_host', '')
EMAIL_HOST_USER = SECRETS.get('email_host_user', '')
EMAIL_HOST_PASSWORD = SECRETS.get('email_host_password', '')
