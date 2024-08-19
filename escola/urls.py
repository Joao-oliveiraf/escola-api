from django.urls import path,include
from .views import EstudanteViewSet, CursoViewSet, MatriculaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls))
]