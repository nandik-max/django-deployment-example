# from django.conf.urls import url
from basic_app import views
from django.contrib import admin
from django.urls import path
# from first_app import views
# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
