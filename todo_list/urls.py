from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', ListOfDo.as_view(), name='todo_home'),
    path('add_todo/', views.add_todo),
    path('mark_as_todo/<int:id>', mark_as_todo, name='mark_as_todo'),
    path('mark_as_complete/<int:id>', mark_as_complete, name='mark_as_complete'),
    path('edit_todo/<int:id>', edit_todo, name='edit_todo'),
    path('delete_todo/<int:id>', delete_todo, name='delete_todo'),
    path('update_todo/<int:id>', update_todo, name='update_todo'),
]
