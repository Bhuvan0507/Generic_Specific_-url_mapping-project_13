from django.urls import path
from Specific.views import *

app_name='Specific'

urlpatterns=[
    path('uday/',uday,name='uday'),
    path('venkatesh/',venkatesh,name='venkatesh'),
]