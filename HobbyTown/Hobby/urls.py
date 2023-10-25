from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('send_mail/<slug:event_slug>/',send_mail,name='send_mail'),
    path('api/v1/get_form/',ShowAPIView.as_view()),
]
