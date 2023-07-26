from celery import shared_task
@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def get_email(x, y):
    print(x + y)
