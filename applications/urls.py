from django.urls import path
from .views import *

urlpatterns = [
    path('send_email/<int:message_id>', send_email, name='send_email'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeApp.as_view(), name='home'),
    path('accepted/', HomeByAccepted.as_view(), name='accepted'),
    path('new/', HomeByNew.as_view(), name='new'),
    path('close/', HomeByClosed.as_view(), name='close'),
    path('message/<int:pk>', GetMessage.as_view(), name='message'),
    # path('message/<int:pk>', NewGetMessage.as_view(), name='message'),
    path('spec/<int:specialist_id>', GetSpecialist.as_view(), name='specialist'),
    # path('order/add_order', add_order, name='add_order'),
    path('open_order/<int:message_id>', OpenOrder.as_view(), name='open_order'),
    # path('close_order/<int:message_id>', close_order, name='close_order'),
    path('close_order/<int:message_id>', CloseOrder.as_view(), name='close_order'),
    path('delete/<int:message_id>', DeleteOrder.as_view(), name='delete'),
    path('order/add_order', CreateOrder.as_view(), name='add_order'),
    path('accepted_by_user/', AcceptedByUser.as_view(), name='accepted_by_user'),
    # path('delete_chat_message/<int:chat_id>/<int:chat_message_id>', delete_chat_message, name='delete_chat_message'),
    path('message_open_order/<int:message_id>', message_open_order, name='message_open_order'),

]
