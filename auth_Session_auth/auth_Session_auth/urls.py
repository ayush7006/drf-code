from django.contrib import admin
from api import views
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('studentapi', views.StudentViewset,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'),name='rest_framework'),
]
