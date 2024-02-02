
# myapp/urls.py
# from django.urls import path
# from .views import TaskViewSet

# urlpatterns = [
#     path('tasks/', TaskViewSet.as_view(), name='task-list'),
    # path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-detail'),
# ]





# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
