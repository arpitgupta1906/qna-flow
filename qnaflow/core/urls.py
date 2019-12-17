from django.urls import path
from django.conf.urls import url
from . import views

app_name='core'

urlpatterns=[
    path('signup1/',views.SignUp1.as_view(),name='signup1'),
    path('signup2/',views.SignUp2.as_view(),name='signup2'),
]
