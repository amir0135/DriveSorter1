from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet, UserProfileViewSet, test_view, search_files

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'files', FileViewSet)
router.register(r'userprofiles', UserProfileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('test/', test_view, name='test'),  # Existing test view path
    path('search/', search_files, name='search'),  # New search endpoint
]
