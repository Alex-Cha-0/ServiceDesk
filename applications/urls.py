from django.urls import path
from .views import *

app_name = 'applications'

urlpatterns = [
    path('send_email/<int:message_id>', send_email, name='send_email'),
    path('add_category/<int:message_id>', close_order, name='close_order'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', HomeApp.as_view(), name='home'),
    path('accepted/', HomeByAccepted.as_view(), name='accepted'),
    path('new/', HomeByNew.as_view(), name='new'),
    path('close/', HomeByClosed.as_view(), name='close'),
    path('message/<int:pk>', GetMessage.as_view(), name='message'),

    path('spec/<int:specialist_id>', GetSpecialist.as_view(), name='specialist'),

    path('open_order/<int:message_id>', OpenOrder.as_view(), name='open_order'),

    path('delete/<int:message_id>', DeleteOrder.as_view(), name='delete'),
    path('add_order/', CreateOrder.as_view(), name='add_order'),
    path('accepted_by_user/', AcceptedByUser.as_view(), name='accepted_by_user'),

    path('message_open_order/<int:message_id>', message_open_order, name='message_open_order'),
    path('cabinet/<int:pk>', Cabinet.as_view(), name='cabinet'),
    path('add_spec/<int:message_id>', add_spec, name='add_spec'),
    path('extend_the_period/<int:message_id>', extend_the_period, name='extend_the_period')

]
