from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

('DJANGO_SETTINGS_MODULE', 'storis_bro.settings')

app = Celery('storis_bro')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
