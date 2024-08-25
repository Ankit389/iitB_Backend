from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myApp.views import CourseViewSet, CourseInstanceViewSet, home

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'instances', CourseInstanceViewSet)

urlpatterns = [
     path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/instances/<int:year>/<int:semester>/', CourseInstanceViewSet.as_view({'get': 'list'})),
    path('api/instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
]