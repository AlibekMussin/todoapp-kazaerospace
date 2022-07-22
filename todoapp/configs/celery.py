# Vendor
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('todoapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
