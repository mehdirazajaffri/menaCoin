from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery
from celery.schedules import crontab

logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'menaCoin.settings')
app = Celery('menaCoin')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-1-hour': {
        'task': 'api.tasks.get_btc_exchange_rate',
        'schedule': crontab(hour="*"),
    },
}
