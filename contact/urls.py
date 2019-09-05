from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'all_users', views.UserViewSet)

urlpatterns = [
    path('new/', views.newUser),
    path('', include(router.urls)),
    # path('all_users/', views.UserList.as_view())
]
