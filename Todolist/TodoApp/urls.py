from django.urls import path
from .view import alltodos
from .view import deleteItem

urlpatterns=[
    path('',alltodos,name='alltodos'),
   path('delete/<int:pk>/',deleteItem, name='deleteitem')

]