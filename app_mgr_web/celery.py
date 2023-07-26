import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_mgr_web.settings')
celery_app = Celery('app_mgr_web')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
