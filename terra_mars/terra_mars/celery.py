from __future__ import absolute_import, unicode_literals

import django
from celery import Celery

django.setup()

app = Celery("terra_mars")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
