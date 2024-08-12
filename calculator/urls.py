from django.urls import path
from .views import add_numbers_view

urlpatterns = [
    path('', add_numbers_view, name='add-numbers'),
]
