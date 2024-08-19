from django.urls import path
from .views import estudante, EstudanteView

urlpatterns = [
    path('estudante/', EstudanteView.as_view())
]