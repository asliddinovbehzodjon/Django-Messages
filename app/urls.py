from django.urls import path

from .views import *

urlpatterns = [
    path('',first,name='first'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',update,name='update'),
]
