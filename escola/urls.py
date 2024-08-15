from django.urls import path
from .views import estudante

urlpatterns = [
    path('estudante/', estudante)
]