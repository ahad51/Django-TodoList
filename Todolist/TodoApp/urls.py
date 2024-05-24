from django.urls import path
from .view import alltodos

urlpatterns=[
    path('',alltodos,name='alltodos')
]