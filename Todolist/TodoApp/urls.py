from django.urls import path
from .view import deleteItem,updateItem,alltodos


urlpatterns = [
    path('', alltodos, name='alltodos'),
    path('delete_item/<int:pk>/', deleteItem, name='deleteitem'),
    
    path('update_item/<int:pk>/', updateItem, name='updateitem')
]