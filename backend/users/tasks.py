from django.core import management

from pentam import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
