from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import add_student, student_list, StudentViewSet

# DRF API
router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('', student_list, name='student_list'),
    path('api/', include(router.urls)), 
]