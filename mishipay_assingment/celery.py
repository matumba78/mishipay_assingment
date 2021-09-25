import os

from celery import Celery
from celery.schedules import crontab


# Setting the default Django settings module for the 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mishipay_assingment.settings')

app = Celery('mishipay_assingment')

#all celery related keys shouldhave CELERY prifix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    # Executes every 5 minutes
    'run-every-5-mins': {
        'task': 'shopify.tasks.sync_shopify_listing_products',
        'schedule': crontab(minute=5)
    }
}