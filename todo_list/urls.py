from django.urls import path
from .views import *

urlpatterns = [
    path('', ListOfDo.as_view(), name='todo_home'),
]
