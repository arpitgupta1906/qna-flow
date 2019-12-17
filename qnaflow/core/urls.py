from django.urls import path
from django.conf.urls import url
from . import views

app_name='core'

urlpatterns=[
    path('signup/',views.SignUp.as_view,name='signup'),
]
